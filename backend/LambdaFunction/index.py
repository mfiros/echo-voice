import itertools
import json
import time
import boto3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dynamodb = boto3.resource('dynamodb')
dynamodb_table = os.environ.get('TABLE_NAME')
table = dynamodb.Table(dynamodb_table)


def split_number(number):
    """
    Splits a given number into three parts of length 3, 3, and the remaining.
    Args:
        number (int): The number to be split.
    Returns:
        tuple: Three parts of the number.
    """
    number = str(number)
    part1 = number[:3]
    part2 = number[3:6]
    part3 = number[6:]
    return part1, part2, part3


def load_dictionary(file_path):
    """
    Loads a dictionary from a JSON file.
    Args:
        file_path (str): The path to the JSON file.
    Returns:
        dict: The loaded dictionary.
    """
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary


def get_replacements(number, dictionary):
    """
    Retrieves the replacements for a given number from the dictionary.
    Args:
        number (str): The number for which replacements are needed.
        dictionary (dict): The dictionary containing number-word mappings.
    Returns:
        list: A list of words that can replace the given number.
    """
    replacements = []
    if number in dictionary.values():
        words = [key for key, value in dictionary.items() if value == number]
        replacements.append(words)
    # print(replacements)
    return replacements


def generate_combinations(replacements_list):
    """
    Generates all possible combinations of replacements.
    Args:
        replacements_list (list): A list of replacement options.
    Returns:
        list: All possible combinations of replacements.
    """
    if not replacements_list:
        return [[]]
    combinations = []
    for word in replacements_list:
        for sub_combination in generate_combinations(replacements_list[1:]):
            combinations.append([word] + sub_combination)
    # print(combinations)
    return combinations


def convert_number_to_text(number):
    """
    Converts a given number into a list of text representations.
    Args:
        number (int): The number to be converted.
    Returns:
        list: A list of text representations of the number.
    """
    dictionary3 = load_dictionary('words_dictionary3.json')
    dictionary4 = load_dictionary('words_dictionary4.json')

    part1, part2, part3 = split_number(number)

    replacements_part1 = get_replacements(part1, dictionary3)
    replacements_part2 = get_replacements(part2, dictionary3)
    replacements_part3 = get_replacements(part3, dictionary4)
    print(replacements_part1, replacements_part2, replacements_part3)

    combinations_part1 = generate_combinations(replacements_part1)
    combinations_part2 = generate_combinations(replacements_part2)
    combinations_part3 = generate_combinations(replacements_part3)

    results = []
    for combo_part1 in combinations_part1:
        for combo_part2 in combinations_part2:
            for combo_part3 in combinations_part3:
                result = f"{combo_part1[0] if combo_part1 else part1}-{combo_part2[0] if combo_part2 else part2}-{combo_part3[0] if combo_part3 else part3}"
                results.append(result)
    # print(result)
    return results


def parse_combinations(combinations_string):
    """
    Parses combinations string and generates a list of combinations.
    Args:
        combinations_string (str): The string containing combinations.
    Returns:
        list: A list of combinations.
    """
    combinations = combinations_string.split('-')
    parsed_combinations = []
    for combination in combinations:
        parsed_combination = []
        if combination.startswith("['") and combination.endswith("']"):
            words = combination[2:-2].split("', '")
            parsed_combination.extend(words)
        else:
            parsed_combination.append(combination)
        parsed_combinations.append(parsed_combination)

    generated_combinations = list(itertools.product(*parsed_combinations))
    generated_combinations = ['-'.join(combination)
                              for combination in generated_combinations]
    return generated_combinations


def score_item(item, combinations):
    words = item.split('-')
    unique_first_word = words[0]  # Get the first word
    num_unique_first_word = sum(
        1 for item in combinations if item.split('-')[0] == unique_first_word)

    # Calculate the score based on the scoring criteria
    score = num_unique_first_word

    return score


def store_result_in_dynamodb(number, result):

    epoch_time = int(time.time())

    table.put_item(
        Item={
            'callerNumber': number,
            'result': result[:5],
            'calledOn': epoch_time
        }
    )
    logger.info("Stored result in DynamoDB")


def generate_result_string(result):
    resultstring = ""

    if len(result) == 1:
        if any(char.isalpha() for char in result[0]):
            resultstring = "Only one vanity phone number option available: {}. Enjoy your personalized number!".format(
                result[0])
        else:
            resultstring = "I'm sorry, but there are no vanity phone numbers available for your phone number."
    else:
        resultstring = "Here are {} vanity phone number options based on your phone number. ".format(
            len(result))
        for i in range(len(result)):
            resultstring += "Option {}: {}. ".format(i+1, result[i])

    return resultstring


def lambda_handler(event, context):
    logger.info("Received event: %s", event)

    try:
        number = event['Details']['ContactData']['CustomerEndpoint']['Address']
        number = number[3:]  # Remove +91 from the number

        existing_item = table.get_item(Key={'callerNumber': number})
        if 'Item' in existing_item:
            logger.info("Item already exists in DynamoDB: %s",
                        existing_item['Item'])
            # update the calledOn timestamp
            epoch_time = int(time.time())
            table.update_item(
                Key={
                    'callerNumber': number
                },
                UpdateExpression="set calledOn = :c",
                ExpressionAttributeValues={
                    ':c': epoch_time
                },
                ReturnValues="UPDATED_NEW"
            )

            result = existing_item['Item']['result']
            resultstring = generate_result_string(result)
            logger.info("Result string: %s", resultstring)

            resultMap = {
                'CallerNumber': number,
                'Result': resultstring,
            }
            return resultMap

        results = convert_number_to_text(number)
        combinations = parse_combinations(results[0])
        logger.info("Combinations: %s", combinations)

        sorted_data = sorted(combinations, key=lambda item: score_item(
            item, combinations), reverse=True)

        unique_first_parts = set()
        result = []
        for item in sorted_data:
            first_part = item.split('-')[0]
            if first_part not in unique_first_parts:
                result.append(item)
                unique_first_parts.add(first_part)
                if len(result) >= 5:
                    break

        if len(result) < 5:
            for item in sorted_data:
                if item not in result:
                    result.append(item)
                    if len(result) >= 5:
                        break

        logger.info("Sorted data: %s", sorted_data)
        logger.info("Result: %s", result[:5])

        store_result_in_dynamodb(number, result)

        resultstring = generate_result_string(result)
        logger.info("Result string: %s", resultstring)

        resultMap = {
            'CallerNumber': number,
            'Result': resultstring
        }
        return resultMap

    except Exception as e:
        logger.exception("An error occurred during execution")
        return {
            'error': str(e)
        }

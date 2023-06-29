# echo-voice

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.
Demo: https://echo-voice.vercel.app/

```
📦echo-voice
┣ 📂.aws-sam
┃ ┣ 📂build
┃ ┃ ┣ 📂DynamoDBFunction
┃ ┃ ┃ ┣ 📜index.py
┃ ┃ ┃ ┗ 📜**init**.py
┃ ┃ ┣ 📂LambdaFunction
┃ ┃ ┃ ┣ 📜index.py
┃ ┃ ┃ ┣ 📜words_dictionary3.json
┃ ┃ ┃ ┣ 📜words_dictionary4.json
┃ ┃ ┃ ┗ 📜**init**.py
┃ ┃ ┗ 📜template.yaml
┃ ┣ 📂cache
┃ ┣ 📂deps
┃ ┗ 📜build.toml
┣ 📂frontend
┃ ┗ 📂echo-voice
┃ ┃ ┣ 📂public
┃ ┃ ┃ ┣ 📜next.svg
┃ ┃ ┃ ┗ 📜vercel.svg
┃ ┃ ┣ 📂src
┃ ┃ ┃ ┗ 📂app
┃ ┃ ┃ ┃ ┣ 📂components
┃ ┃ ┃ ┃ ┃ ┗ 📜main.js
┃ ┃ ┃ ┃ ┣ 📜favicon.ico
┃ ┃ ┃ ┃ ┣ 📜globals.css
┃ ┃ ┃ ┃ ┣ 📜layout.js
┃ ┃ ┃ ┃ ┗ 📜page.js
┃ ┃ ┣ 📜.env.example
┃ ┃ ┣ 📜.gitignore
┃ ┃ ┣ 📜jsconfig.json
┃ ┃ ┣ 📜next.config.js
┃ ┃ ┣ 📜package-lock.json
┃ ┃ ┣ 📜package.json
┃ ┃ ┣ 📜postcss.config.js
┃ ┃ ┣ 📜README.md
┃ ┃ ┗ 📜tailwind.config.js
┣ 📂backend
┃ ┣ 📂DynamoDBFunction
┃ ┃ ┣ 📜index.py
┃ ┃ ┗ 📜**init**.py
┃ ┗ 📂LambdaFunction
┃ ┃ ┣ 📂helper
┃ ┃ ┃ ┣ 📜english.txt
┃ ┃ ┃ ┗ 📜generate_dic.py
┃ ┃ ┣ 📜index.py
┃ ┃ ┣ 📜words_dictionary3.json
┃ ┃ ┣ 📜words_dictionary4.json
┃ ┃ ┗ 📜**init**.py
┣ 📜.gitignore
┣ 📜README.md
┣ 📜samconfig.toml
┣ 📜template.yaml
```

- Backend - Code for the application's Lambda function
- Frontend - Code for the application's frontend
- template.yaml - A template that defines the application's AWS resources
- README.md - This file
- samconfig.toml - SAM CLI configuration file

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Requirements

- AWS CLI already configured with Administrator permission
- AWS SAM CLI already installed
- [Python 3 installed](https://www.python.org/downloads/)

## AWS Resources

- Lambda Function: `DynamoDBFunction, GenerateVanityFunction`
- DynamoDB: `DynamoDBTable`
- API Gateway: `FetchCallersApi`
- IAM: `GenerateVanityFunctionRole, DynamoDBFunctionRole, ConnectInstanceAttachRole`
- Connect: `ConnectFlowContactFlow`

## Deploy the sample application

To build and deploy your application for the first time, run the following in your shell:

```bash
Clone the repository
git clone https://github.com/mfiros/echo-voice.git
cd echo-voice
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

```bash
Configuring SAM deploy
======================

    Looking for config file [samconfig.toml] :  Found
    Reading default arguments  :  Success

    Setting default arguments for 'sam deploy'
    =========================================
    Stack Name [sam-app]: echo-voice
    AWS Region [us-east-1]: us-east-1
    Parameter ConnectInstance [arn:aws:connect:us-east-1:1234565:instance/dce2318b-1234-1234-1234-123456789012]: arn:aws:connect:us-east-1:1234565:instance/dce2318b-1234-1234-1234-123456789012

    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
    Confirm changes before deploy [y/N]: y
    #SAM needs permission to be able to create roles to connect to the resources in your template
    Allow SAM CLI IAM role creation [Y/n]: Y
    Save arguments to configuration file [Y/n]: Y
    SAM configuration file [samconfig.toml]: samconfig.toml
    SAM configuration environment [default]: default

    Looking for resources needed for deployment: Found!


    Deploying with following values
    ===============================
    Stack name                   : echo-voice
    Region                       : us-east-1
    Confirm changeset            : True
    Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-1j2j2j2j2j2j
    Capabilities                 : ["CAPABILITY_NAMED_IAM"]
    Parameter overrides          : {"ConnectInstance": "arn:aws:connect:us-east-1:1234556:instance/dce2318b-1234-1234-1234-123456789012"}
    Signing Profiles             : {}

Initiating deployment
=====================
CloudFormation stack changeset
---------------------------------------------------------------------------------------------------------------------
Operation                     LogicalResourceId             ResourceType                  Replacement
---------------------------------------------------------------------------------------------------------------------
+ Add                         CognitoUserPoolClient         AWS::Cognito::UserPoolClien   N/A
                                                            t
+ Add                         CognitoUserPoolDomain         AWS::Cognito::UserPoolDomai   N/A
                                                            n
+ Add                         CognitoUserPool               AWS::Cognito::UserPool        N/A
+ Add                         ConnectFlowContactFlow        AWS::Connect::ContactFlow     N/A
+ Add                         ConnectInstanceAttachRole     AWS::Lambda::Permission       N/A
+ Add                         DynamoDBFunctionFetchCaller   AWS::Lambda::Permission       N/A
                              sPermissionProd
+ Add                         DynamoDBFunctionRole          AWS::IAM::Role                N/A
+ Add                         DynamoDBFunction              AWS::Lambda::Function         N/A
+ Add                         DynamoDBTable                 AWS::DynamoDB::Table          N/A
+ Add                         FetchCallersApiDeployment71   AWS::ApiGateway::Deployment   N/A
                              09639b61
+ Add                         FetchCallersApiProdStage      AWS::ApiGateway::Stage        N/A
+ Add                         FetchCallersApi               AWS::ApiGateway::RestApi      N/A
+ Add                         GenerateVanityFunctionRole    AWS::IAM::Role                N/A
+ Add                         GenerateVanityFunction        AWS::Lambda::Function         N/A
---------------------------------------------------------------------------------------------------------------------

Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

2023-06-29 13:33:44 - Waiting for stack create/update to complete

CloudFormation events from stack operations (refresh every 5.0 seconds)
---------------------------------------------------------------------------------------------------------------------
ResourceStatus                ResourceType                  LogicalResourceId             ResourceStatusReason
---------------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS            AWS::DynamoDB::Table          DynamoDBTable                 -
CREATE_IN_PROGRESS            AWS::Cognito::UserPool        CognitoUserPool               -
CREATE_IN_PROGRESS            AWS::DynamoDB::Table          DynamoDBTable                 Resource creation Initiated


```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "echo-voice"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

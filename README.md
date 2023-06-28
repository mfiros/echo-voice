# echo-voice

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

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
┗ 📜**init**.py
```

- Backend - Code for the application's Lambda function
- Frontend - Code for the application's frontend
- template.yaml - A template that defines the application's AWS resources
- README.md - This file
- samconfig.toml - SAM CLI configuration file

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Requirements

- AWS CLI already configured with Administrator permission
- [Python 3 installed](https://www.python.org/downloads/)

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name "echo-voice"
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

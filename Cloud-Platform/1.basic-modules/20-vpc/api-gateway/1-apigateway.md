# Pre-Requisites and Lambda Deployment
In order to complete this immersion day lab, you will need the following:

- AWS CLI - Follow the AWS CLI Getting Started guide  to install and configure the CLI on your machine.

- CostCalculator and MedianPriceCalculator Lambda Functions

- Postman - https://www.postman.com/downloads/ 

The code and instructions in this workshop assume only one person is using a given AWS account at a time and that all resources are in us-east-1 region.

## Deploy Lambda Functions

1. Download the Serverless Application Model (SAM) template package-template.yaml 

2. Run the following command to configure your AWS CLI

```
$ aws configure
AWS Access Key ID [None]: <Enter Access Key ID>
AWS Secret Access Key [None]: <Enter Secret key>
Default region name [None]: us-east-1
Default output format [None]: json
```

Note for users with Federated AWS console login or SSO
If you use Federated logins or SSO set your environment variables instead for the following (you may need to reach out to your IT Admin on how to obtain temporary credentials):

```
$Env:AWS_DEFAULT_REGION="us-east-1"
$Env:AWS_ACCESS_KEY_ID="xxx"
$Env:AWS_SECRET_ACCESS_KEY="xxx"
$Env:AWS_SESSION_TOKEN="xxx"
```

3. Run the following command to deploy the lambda functions

```
aws cloudformation deploy --template-file path-to-template-file/packaged-template.yaml --stack-name serverless-immersion-day-stack --capabilities CAPABILITY_IAM
```

The above command deploys two lambda functions. Below is a description of each function and the applicable lab sections.

Function Name | Description	Lab | Usage
------------- | --------------- | -----
CostCalculator | Lambda function that calculates the price per unit and the total cost of a house.Price per unit = price/sizeTotal cost = downpaymentAmount + price	Main Sections
MedianPriceCalculator | Lambda function that returns the median price of a house in US ($320,000) and Canada ($240,000).	Optional Sections

Once the above command is executed, you can verify the deployment of these functions by going to the lambda console.

4. Go to the Lambda console at https://console.aws.amazon.com/lambda 

5. Verify that serverless-immersion-day-api-CalculateCostPerUnit-XX and serverless-immersion-day-api-MedianPriceCalculator-XX are listed.

![](../../images/1-apigateway)

You are now ready to start the lab!

[Previous](../api-gateway.md) | [Next](../api-gateway/2-apigateway.md)
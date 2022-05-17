# Create Your First API

1. Sign into the AWS Management Console and open Amzon API Gateway console at https://console.aws.amazon.com/apigateway 

2. If this is your first API, you will see the Amazon API Gateway welcome page.

![](../../images/Figure2-ApiGatewayFirstUse.png)

- Click on Build under REST API. Click Ok on the popup

![](../../images/Figure2-1-APIGatewayFirstUsePopup.png)

- Otherwise, click APIs then Create API. - Click on Build under REST API.

![](../../images/Figure2-2-CreateAPI.png)

1. Under Create New API Select New API

2. Under Settings, Enter the following values:
    - API Name: calculatePrice

    - Description: Calculates the price of a house per square meters

    - Endpoint Type: Regional

![](../../images/Figure3-CreatingANewAPI.png)

5. Click Create API

6. Under Actions, choose Create Resource

![](../../images/Figure4-CreatingANewResource.png)

7. Enter the following values:
    
    - Resource Name: pricePerMeter

8. Click Create Resource

![](../../images/Figure5-ResourceNameAndPath.png)

9. Select Actions, choose Create Method

![](../../images/Figure6-CreatingAMethod.png)

10. Choose Post and Click on check icon to confirm.

![](../../images/Figure6-1-SelectPostOnMethod.png)

11. Under the Post method, Choose the following values:

    - Integration Type: Lambda Function

    - Lambda Region: us-east-1

    - Lambda Function: serverless-immersion-day-stac-CalculateCostPerUnit- (Select the function which comes up.)

12. Click Save.

![](../../images/Figure7-ConfiguringPOSTAction.png)

13. In the dialogue box, Add Permission to Lambda Function, Click OK.

You have now configured your API to call the costCalculator lambda function. The API Gateway pane shows the request and response flow of data.

![](../../images/Figure8-APIGatewayConsolePane.png)

14. Click on the Test icon to provide a sample request message.

15. Copy and Paste the following JSON Sample in the Request Body section

```
{
  "price": "400000",
  "size": "1600",
  "unit": "sqFt",
  "downPayment": "20"
} 
```

16. Click Test

Please note the Response Body with a status code of 200. The body of the response contains the price per unit and the total cost. The header of the response along with the message body is composed by the lambda function. The testing page also shows a complete request/response log.

![](../../images/Figure9-TestingAPI.png)

Notice that the lambda service returned the total cost, but did not account for the down payment. In the next section, we will transform the message to pass the down payment amount to the lambda function.

[Previous](./1-apigateway.md) | [Next](./3-apigateway.md)
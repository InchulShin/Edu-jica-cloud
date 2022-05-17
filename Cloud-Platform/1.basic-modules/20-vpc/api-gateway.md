# Amazon API Gateway Hands on Lab

## Amazon API Gateway Overview
Amazon API Gateway  is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs, HTTP APIs, or WebSocket APIs (which enable real-time two-way communication applications). API Gateway supports containerized and serverless workloads, as well as web applications.

API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, CORS support, authorization and access control, throttling, monitoring, and API version management. API Gateway has no minimum fees or startup costs. You pay for the API calls you receive and the amount of data transferred out and, with the API Gateway tiered pricing model, you can reduce your cost as your API usage scales.

![](../images/lab-architecture.svg)

In the main lab sections, you will create an API that invokes a lambda function to calculate the price of a house (price per square foot). In the first part of the lab, you will deploy a pre-defined sample lambda function and create the back-end API. You will test your APIs using both the API Gateway console and Postman.

In the optional lab sections, you will learn how to cache service responses, throttle requests, and create various usage plans.

The overall architecture for the lab is depicted above.

Configure your own API Gateway by going through the labs in the order below:

- Pre-Requisites and Lambda Deployment

- Create Your First API

- Message Transformation

- Request Validation

- Authentication and Authorization

- API Deployment

- Message Caching (Optional)

- Usage Plans and Message Throttling (Optional)

- Clean Up Resources

[Previous](../20-vpc/vpc/6-vpc.md) | [Next](../api-gateway.md)
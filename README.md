# Backend Coding Test - Word Counter
Design an API which counts how many times a word exists in a webpage 
source.
## Getting Started
Design an API with serverless aws: api gateway, lambda function and dynamodb to store result.
A serverless architecture is a way to build and run applications and services without having to manage infrastructure. Your application still runs on servers, but all the server management is done by AWS.
## Prerequisites
aws account and access to services: api gateway, lambda function and dynamodb.
## Deployment
[wordcount](https://7te95zu8qa.execute-api.ap-northeast-1.amazonaws.com/prod/wordcount) 
https://7te95zu8qa.execute-api.ap-northeast-1.amazonaws.com/prod/wordcount
## Test
Post: { "word": "fit", "url": "https://www.virtusize.jp/"}
![alt text](https://image.noelshack.com/fichiers/2019/11/7/1552852462-screen.png)
## Result
{"status": 200,"count": 5} 
![alt text](https://image.noelshack.com/fichiers/2019/11/7/1552852581-screen4.png)
## Quality of code
Global evaluation
-----------------
Your code has been rated at 6.40/10 

# Backend Coding Test - Word Counter
Design an API which counts how many times a word exists in a webpage 
source.
## Getting Started
Design an API with serverless aws: api gateway, lambda function and dynamodb to store result.
## Prerequisites
aws account and access to services: api gateway, lambda function and dynamodb.
## Deployment
[wordcount](https://7te95zu8qa.execute-api.ap-northeast-1.amazonaws.com/prod/wordcount) 
https://7te95zu8qa.execute-api.ap-northeast-1.amazonaws.com/prod/wordcount
## Test
Post: { "word": "fit", "url": "https://www.virtusize.jp/"}
![alt text](https://drive.google.com/file/d/1BJ7TGMkG-wxzjbuzTz2cNEmsNE5KIq3c/view)
## Result
{"status": 200,"count": 5} 

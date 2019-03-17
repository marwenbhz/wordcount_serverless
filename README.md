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
![alt text](https://helpx.adobe.com/content/dam/help/en/stock/how-to/visual-reverse-image-search/_jcr_content/main-pars/image/visual-reverse-image-search-v2_1000x560.jpg)
Post: { "word": "fit", "url": "https://www.virtusize.jp/"}
## Result
{"status": 200,"count": 5} 

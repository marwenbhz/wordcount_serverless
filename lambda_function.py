import boto3
from botocore.vendored import requests


def lambda_handler(event):
    client = boto3.client('dynamodb')
    try:
        url = str(event['url'])
    except Exception:
        return {"message": "missing url in input !"}
    try:
        word = str(event['word'])
    except Exception:
        return {"message": "missing word in input !"}
    try:
        r = requests.get(url)
        status = r.status_code
        if status == 200:
            count = r.text.count(word)
            response = {"status": status, "count": count}
            # Post to dynamo db
            item_counter = {
                "count": {"N": str(count)},
                "url": {"S": url},
                "word": {"S": word},
                "status": {"N": str(status)}
                }
            client.put_item(
                    TableName='Word_Counter',
                    Item=item_counter
                    )
            return response
        else:
            response = {"status": status, "message": "error in url"}
            return response
    except Exception:
        return {"message": "error in url to fetch !"}

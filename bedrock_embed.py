"""
Shows how to generate embeddings with the Amazon Titan Text Embeddings V2 Model
"""

import json
import logging
import boto3
import pandas as pd


def generate_embeddings(model_id, body):
    ACCESS_KEY = "<AC KEY>"
    SECRET_ACCESS_KEY = "<SEC Key>"
    AWS_REGION = "us-east-1"

    bedrock = boto3.client(service_name='bedrock-runtime',
                           region_name=AWS_REGION,
                           aws_access_key_id=ACCESS_KEY,
                           aws_secret_access_key=SECRET_ACCESS_KEY )

    accept = "application/json"
    content_type = "application/json"

    response = bedrock.invoke_model(
        body=body, modelId=model_id, accept=accept, contentType=content_type
    )

    response_body = json.loads(response.get('body').read())

    return response_body


def main():
    """
    Entrypoint for Amazon Titan Embeddings V2 - Text example.
    """


    model_id = "amazon.titan-embed-text-v2:0"

    df = pd.read_csv(r'C:\Users\sudhi\Downloads\archive\100_Complaints.csv')
    df=df[0:100]
    print(df.columns);
    print(len(df))
    newcol =[]
    i=0


    for index in df.index :
        print ((df["Product"][index]))
        field=df["Consumer complaint narrative"][index]
        body = json.dumps({
            "inputText": field,
            "dimensions": 512,
            "normalize": True
        })
        try:
            print(i)
            i = i+1
            response = generate_embeddings(model_id, body)

            print(f"Generated embeddings: {response['embedding']}")
            print(f"Input Token count:  {response['inputTextTokenCount']}")

        except ClientError as err:
            message = err.response["Error"]["Message"]
            logger.error("A client error occurred: %s", message)
            print("A client error occured: " +
                  format(message))

        newcol.append( response['embedding'])


    outDf = pd.DataFrame({'embeddings': newcol})
    result = pd.concat([df, outDf], axis=1, join="inner")
    print(result)
    result.to_csv(r'C:\Users\sudhi\Downloads\archive\512_Complaints_embed.csv')


if __name__ == "__main__":
    main()

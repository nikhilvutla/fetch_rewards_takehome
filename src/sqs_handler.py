import boto3
from .config import SQS_QUEUE_URL

def get_sqs_client():
    sqs = boto3.client('sqs', endpoint_url=SQS_QUEUE_URL)
    return sqs

def read_from_sqs():
    sqs = get_sqs_client()
    messages = sqs.receive_message(QueueUrl=SQS_QUEUE_URL)
    return messages

from .db_handler import insert_data
from .sqs_handler import read_from_sqs
from .masker import mask_pii

def run_etl():
    messages = read_from_sqs()
    for message in messages:
        masked_data = mask_pii(message)
        insert_data(masked_data)


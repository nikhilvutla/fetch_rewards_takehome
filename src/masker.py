import hashlib

def mask_pii(data):
    # implement the masking logic
    # Here we use SHA256 to mask data
    masked_data = data.copy()
    masked_data["device_id"] = hashlib.sha256(data["device_id"].encode()).hexdigest()
    masked_data["ip"] = hashlib.sha256(data["ip"].encode()).hexdigest()
    return masked_data


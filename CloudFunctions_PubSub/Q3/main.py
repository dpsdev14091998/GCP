import base64
from gcloud import storage

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    pubsub_dict=eval(pubsub_message)
    filenm=pubsub_dict["name"]
    content_pub=pubsub_dict["content"]
    filenm=filenm+".json"
    
    client = storage.Client()
    bucket = client.get_bucket('ad-bucket1')
    blob = bucket.blob(filenm)
    blob.upload_from_string(content_pub)
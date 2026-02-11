import boto3
import uuid
from app.core.config import settings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
)

def upload_image(file):
    filename = f"{uuid.uuid4()}.jpg"
    s3.upload_fileobj(
        file,
        settings.AWS_BUCKET_NAME,
        filename,
        ExtraArgs={"ContentType": "image/jpeg"}
    )
    return f"https://{settings.AWS_BUCKET_NAME}.s3.amazonaws.com/{filename}"

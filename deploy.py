import boto3
import os

BUCKET_NAME = "arn:aws:s3:::my-professional-portfolio-2026-745805181779-us-east-1-an"
WEBSITE_DIR = "./"

s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['AKIA23JLT6NJ2XXILNX3'],
    aws_secret_access_key=os.environ['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']
)

def upload_files():
    for root, dirs, files in os.walk(WEBSITE_DIR):
        for file in files:
            if file.endswith(('.html', '.css', '.js')):
                full_path = os.path.join(root, file)
                s3_path = file

                print(f"Uploading {file}...")
                s3.upload_file(
                    full_path,
                    arn:aws:s3:::my-professional-portfolio-2026-745805181779-us-east-1-an,
                    s3_path,
                    ExtraArgs={'ContentType': get_content_type(file)}
                )

def get_content_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    elif filename.endswith(".css"):
        return "text/css"
    elif filename.endswith(".js"):
        return "application/javascript"
    return "text/plain"

if __name__ == "__main__":
    upload_files()

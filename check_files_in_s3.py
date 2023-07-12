import os
import boto3
from botocore.exceptions import ClientError
import logging
import credentials


params = {"local_folder" : r"C:\Users\pedri\OneDrive\Área de Trabalho\Stuff\Python\Aulas\29-06-23-basic-data\dataset",
          "bucket" : "bucket-data-eng-augusto"}

session = boto3.Session(aws_access_key_id=credentials.access, aws_secret_access_key=credentials.secret, region_name=credentials.region)
rds = session.client('rds')
s3 = session.client('s3')

def check_files_in_s3(s3, bucket, key):
    """ 
    Check if path/files exists inside S3 bucket

    Parameter:
    bucket (str): bucket string
    key (str): object's path like subfolder/file.csv

    Returns:
    Bool: True if path/files already exists 
    """

    try:
        call = s3.head_object(Bucket=bucket, Key=key)
        if call["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return True
    except ClientError as e:
        if e.response["Error"]["Code"] == 404:
            return  False
        

def upload_s3(s3, bucket):
    """ 
    Upload non existing keys to S3.

    Parameter:
    bucket (str): bucket string

    Returns:
    results (dict): details on the keys that were uploaded, not uploaded and those that experienced errors  
    """

    uploaded = []
    not_uploaded = []
    errors = []
    results = {"Files uploaded" : uploaded, "Files not uploaded" : not_uploaded, "Errors encountered" : errors}

    for file in os.listdir(params["local_folder"]):
        if file[-4:] == ".csv":
            filepath = os.path.join(params["local_folder"], file)
            s3_new_folder = file.split(".")[0]
            key = f"{s3_new_folder}/{file}"

            if check_files_in_s3(s3, bucket=bucket, key=key) is False:
                try:
                    s3.upload_file(filepath, Bucket=bucket, Key=key)
                    uploaded.append(key)
                except ClientError as e:
                    logging.error(e)
                    errors.append(key)
            elif check_files_in_s3(s3, bucket=bucket, key=key) is True:
                not_uploaded.append(key)

    print(results)


if __name__ == "__main__":

    upload_s3(s3, bucket=params["bucket"])
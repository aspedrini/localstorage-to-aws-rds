# folder-to-s3-rds

The project goal was to send a dataset from local storage to AWS S3, creating subfolders to each .csv and sending them to a Postgre database located in AWS RDS service.
It's inspiration came after watching a Youtube video from the creator Darshil Parmar, which the main goals were to find a suitable dataset (three tables or more), create diagram of the dataset and send the data to a SQL database. As i'm learning more about AWS and it's services, I aimed to implement it to the cloud.


In the future I plan to make the extract step occur inside Python's memory with IO modules. As the dataset is from Kaggle, it could not be downloaded straight from the URL as it needed login to access. I also intend to automate the proccess with Airflow.

Dataset:
Brazilian E-Commerce Public Dataset by Olist
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download
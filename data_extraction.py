import database_utils as du
import pandas as pd
import tabula
import json
import sqlalchemy as alch
import boto3
import requests
import yaml

# Initialize necessary components and API details
db_connector = du.DatabaseConnector()

with open('db_creds.yaml', 'r') as file:
    creds = yaml.safe_load(file)
    
header_details = creds['x-api-key']
retrieve_stores = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
s3_client = boto3.client('s3')

class DataExtractor:
    def __init__(self):
        self.db = DatabaseConnector()
        self.api_key = header_details.get('x-api-key')

    
    # Read the data from a specified table
    def read_rds_table(self, table_name):
        df = pd.read_sql_table(table_name, self.db.init_db_engine())
        return df

    
    # Retrieving from specified URL
    def retrieve_pdf_data(self):
        retrieve_pdf_df = tabula.read_pdf('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf', pages='all')
        pdf_df = pd.concat(retrieve_pdf_df, ignore_index=True)
        return pdf_df

    
    # Using an API endpoint with authorisation
    def list_number_of_store(self):
        stores = requests.get(retrieve_stores, headers=self.api_key)
        number_of_stores = stores.json()
        return number_of_stores["number_stores"]

    
    # Extract data from an S3 address
    def extract_from_s3(self, s3_address):
        bucket, key = s3_address.replace('s3://', '').split('/', 1)
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        with response['Body'] as body:
            s3_df = pd.read_csv(body)
            return s3_df

    
    # Extract JSON data from a specific file in S3
    def extract_json_data(self):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='data-handling-public', Key='date_details.json')
        json_object = response['Body'].read().decode('utf-8')
        df_date_details = pd.read_json(json_object)
        return df_date_details

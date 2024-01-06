import yaml
import pandas as pd
import sqlalchemy as alch

class DatabaseConnector():
  # Initialize the database engine when the DatabaseConnector object is created
  def __init__(self):
        self.engine = self.init_db_engine()

  
  # Read database credentials from a YAML file
  def read_db_creds(self):
    with open('db_creds.yaml', 'r') as file:
      creds = yaml.safe_load(file)
    return creds

  
  def init_db_engine(self):
    # Read the essential credentials from the .yaml file
    creds = self.read_db_creds()
    host = creds['RDS_HOST']
    user = creds['RDS_USER']
    password = creds['RDS_PASSWORD']
    database = creds['RDS_DB_TYPE']
    port = creds['RDS_PORT']
    db_name = creds['RDS_DATABASE']
    # Create the database URL
    engine = create_engine(f"{database}://{user}:{password}@{host}:{port}/{db_name}")
    return engine.connect()

  
  # List all tables in the connected database using SQLAlchemy
  def list_db_tables(self):
    return alch.inspect(self.init_db_engine()).get_table_names()

  
  def upload_to_db(self, df, table_name):
    with self.engine.connect() as conn:
      try:
        df.to_sql(table_name, conn, index=False)
      except ValueError as err:
        print(err.__str__())
      else:
        print(f"{table_name} T")

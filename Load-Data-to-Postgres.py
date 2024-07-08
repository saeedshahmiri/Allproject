import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os


def load_data(connection_engine):
    # Get the directory path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the file
    file_path = os.path.join(current_dir, "bank-full.csv")
    df = pd.read_csv(file_path)

    df.to_sql("bank-Saeed", connection_engine, if_exists='append', index=False)

if __name__ == '__main__':
    try:
        # Load environment variables from .env file
        
        # Retrieve database connection details from environment variables
        db_username = "consultants"
        db_password = "WelcomeItc%402022"
        db_host = "ec2-3-9-191-104.eu-west-2.compute.amazonaws.com"
        db_port = "5432"
        db_name = "testdb"

        url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

        sql_engine = create_engine(url)

        load_data(connection_engine=sql_engine)

    except Exception as ex:
        print(ex)
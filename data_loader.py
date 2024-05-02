import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

def load_data_from_dataframe_to_postgres(dataframe, table_name, conn_string):
    try:
        engine = create_engine(conn_string)

        dataframe.to_sql(table_name, engine, if_exists='append', index=False)

        print("Data loaded successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error loading data from DataFrame to PostgreSQL:", error)

csv_file = 'healthcare_claims.csv'
table_name = 'healthcare_claims'
conn_string = "postgresql+psycopg2://postgres:password@localhost:5432/postgres"

df = pd.read_csv(csv_file)

load_data_from_dataframe_to_postgres(df, table_name, conn_string)

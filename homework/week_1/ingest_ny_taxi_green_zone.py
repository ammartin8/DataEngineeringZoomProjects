#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import pandas as pd
from sqlalchemy import create_engine
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')


    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output_zones.csv'

    # Download csv

    os.system(f"wget {url} -O {csv_name}")

    # import data to data frame
    df = pd.read_csv(csv_name)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Adding zone data to database
    df.to_sql(name=table_name, con=engine, if_exists="append")
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
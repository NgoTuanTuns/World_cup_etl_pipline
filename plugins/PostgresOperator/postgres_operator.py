from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd
from sqlalchemy import create_engine
import logging
## PostgresOperator
class PostgresOperator:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        try:
            self.hook = PostgresHook(conn_id)
        except Exception as e:
            logging.debug(e)
        
    def get_conn_id(self):
        return self.conn_id

    def get_hook(self):
        return self.hook

    def insert_into_table(self, df, table_name, schema):
        url = self.hook.get_uri()
        engine = create_engine(url)
        df.to_sql(table_name, engine, if_exists = 'replace', schema = schema)
    
    def sql(self, sql_command):
        self.hook.run(sql_command)
    
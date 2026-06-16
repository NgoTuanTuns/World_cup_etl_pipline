import pandas as pd
from postgres_operator import PostgresOperator
def transform_top_scorers():
    op = PostgresOperator('postgres_localhost')
    df_top_scorers = pd.read_csv('datashets/wc_top_scorers.csv')
    op.insert_into_table(df_top_scorers, 'wc_top_scorers', 'dim')
    op.sql("""
        alter table dim.wc_top_scorers
        add constraint pk_top_scorers primary key ("edition")
    """)
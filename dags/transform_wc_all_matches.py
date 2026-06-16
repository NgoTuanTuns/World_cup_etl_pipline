import pandas as pd
from postgres_operator import PostgresOperator
def transform_all_matches():
    op = PostgresOperator('postgres_localhost')
    df_all_matches = pd.read_csv('datashets/wc_all_matches.csv')
    op.insert_into_table(df_all_matches, 'wc_all_matches', 'dim')
    op.sql("""
        alter table dim.wc_all_matches
        add constraint pk_all_matches primary key ("year", "stage", "team1", "team2", "city")
    """)
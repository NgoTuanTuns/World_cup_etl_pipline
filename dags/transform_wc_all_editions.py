import pandas as pd
from postgres_operator import PostgresOperator

def transform_all_editions():
    op = PostgresOperator('postgres_localhost')
    df_editions = pd.read_csv('datashets/wc_all_editions.csv')
    df_excluded = df_editions[
        ['edition',
        'year',
        'host',
        'champion',
        'runner_up',
        'third_place',
        'fourth_place',
        'teams',
        'matches',
        'top_scorer',
        'goals',
        'goals_per_match',
        'attendance',
        'start_date',
        'end_date',
        'final_city',
        'host_won',
        'format']
    ]
    op.insert_into_table(df_excluded, 'wc_all_editions', 'dim')

    op.sql("""
        alter table dim.wc_all_editions
        add constraint pk_wc_all_edition primary key ("edition")
    """)

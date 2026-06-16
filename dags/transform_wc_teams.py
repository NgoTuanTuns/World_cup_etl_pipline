import pandas as pd
from postgres_operator import PostgresOperator

def transform_team_2026():
    op = PostgresOperator('postgres_localhost')
    df_team_2026 = pd.read_csv('datashets/wc_2026_teams.csv')
    op.insert_into_table(df_team_2026, 'wc2026_teams', 'fact')

    op.sql("""
        alter table fact.wc2026_teams
        add constraint pk_wc2026_team primary key ("team")
    """)

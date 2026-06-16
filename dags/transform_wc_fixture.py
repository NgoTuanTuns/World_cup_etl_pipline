import pandas as pd
import datetime
from postgres_operator import PostgresOperator
def transform_fixture_2026():
    op = PostgresOperator('postgres_localhost')
    df_fixtures_2026 = pd.read_csv('datashets/wc_2026_fixtures.csv')
    df_excluded = df_fixtures_2026[
        ['group', 'stage', 'team1', 'team2', 'venue', 'city', 'country', 'date', 'kickoff_et']
    ]
    df_excluded['status'] = "Unknown"
    df_excluded.loc[df_excluded['date'].astype('datetime64[ns]') < datetime.datetime.today(), 'status'] = 'Finished'
    df_excluded.loc[df_excluded['date'].astype('datetime64[ns]') > datetime.datetime.today(), 'status'] = 'About to start'
    df_excluded.loc[df_excluded['group'].isna(), 'group'] = 'None'
    op.insert_into_table(df_excluded, 'wc2026_fixtures', 'dim')

    op.sql("""
        alter table dim.wc2026_fixtures
        add constraint pk_gr_st primary key ("group", "stage", "team1", "team2", "city")
    """)
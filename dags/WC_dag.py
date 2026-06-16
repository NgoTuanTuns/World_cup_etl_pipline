from airflow import DAG
import pandas as pd
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from transform_wc_fixture import transform_fixture_2026
import logging
from transform_wc_teams import transform_team_2026
from transform_wc_top_scorers import transform_top_scorers
from transform_wc_all_editions import transform_all_editions
from transform_wc_all_matches import transform_all_matches
default_args = {
    'owner':'tu',
    'retries':2,
    'retry_delay':timedelta(1)
}

with DAG (
    dag_id = 'WC_dag_v8',
    default_args = default_args,
    start_date = datetime(2026,6,1),
    schedule = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'transform_teams_table',
        python_callable = transform_team_2026
    )

    task2 = PythonOperator(
        task_id = 'transform_fixture_table',
        python_callable = transform_fixture_2026
    )

    task3 = PythonOperator(
        task_id = 'transform_wc_top_scorers_table',
        python_callable = transform_top_scorers
    )

    task4 = PythonOperator(
        task_id = 'transform_wc_all_editions_table',
        python_callable = transform_all_editions
    )

    task5 = PythonOperator(
        task_id = 'transform_wc_all_matches_table',
        python_callable = transform_all_matches
    )

    task1
    task2
    task3
    task4
    task5
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import logging
from python_to_postgres import MyDatabase


def task_3_put_data():
    try:
        engine = create_engine("postgresql://postgres:9431@localhost:5433/employees")
        Session = sessionmaker(bind=engine)

        with Session() as session:
            xlsx_path = "/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_2.xlsx"
            df = pd.read_excel(xlsx_path)
            # Uploading from excel to database
            df.to_sql('task_2_duplicate', engine, if_exists="replace", index=False)
    except Exception as e:
        logging.error(e)


def read_task_3_data():
    try:
        db = MyDatabase()
        # For reading the newly created table
        select_pipeline = "select * from task_2_duplicate"
        result = db.query(select_pipeline)
        logging.debug(f"Query Executed- {select_pipeline}")
        return result
    except:
        logging.error("Failed to fetch cursor from Database")
    finally:
        db.close()


def task_3():

    # Duplicate the data from xlxs and upload on PostgreSQL
    task_3_put_data()
    # Read the Data
    result = read_task_3_data()
    print(result)

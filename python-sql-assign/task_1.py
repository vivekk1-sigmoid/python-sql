from python_to_postgres import MyDatabase
from utils import convert_to_xlsx_for_task_1
import logging


def task_1_select_query():
    try:
        db = MyDatabase()
        # Query to list out Emp no, Emp name and their managers.
        query_pipeline = "select emp1.empno, emp1.ename, emp2.ename from emp as emp1 INNER JOIN emp as emp2 on (emp1.mgr = emp2.empno);"
        result = db.query(query_pipeline)
        logging.debug(f"Query Executed- {query_pipeline}")
        return result
    except:
        logging.error("Failed to fetch cursor from Database")
    finally:
        db.close()


def task_1():
    path = "/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_1.xlsx"
    # To convert into xlxs with required headers
    convert_to_xlsx_for_task_1(task_1_select_query(), path)
from python_to_postgres import MyDatabase
from utils import convert_to_xlsx_for_task_2
import logging


def task_2_update():
    try:
        db = MyDatabase()
        # Updating to current_date where enddate is NULL
        update_pipeline = "UPDATE jobhist SET enddate = current_date \
           where enddate is NULL;"
        db.update(update_pipeline)
        logging.debug(f"Query Executed- {update_pipeline}")
    except:
        logging.error("Failed to execute the query")
    finally:
        db.close()


def task_2_select():
    try:
        db = MyDatabase()
        # Listing the compensation
        select_pipeline = """SELECT emp.ename, jh.empno, dept.dname,round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,round((enddate - startdate)/30) as emp_month_spent from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"""
        result = db.query(select_pipeline)
        logging.debug(f"Query Executed- {select_pipeline}")
        return result
    except:
        logging.error("Failed to execute the query")
    finally:
        db.close()


def task_2():
    task_2_update()
    # Path to store the xlxs
    path = "/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_2.xlsx"
    convert_to_xlsx_for_task_2(task_2_select(), path)
    print(task_2_select())
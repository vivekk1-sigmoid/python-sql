import logging
import pandas as pd
from utils import convert_to_xlsx_for_task_2_4
from python_to_postgres import MyDatabase


def task_4_group_by():
    try:
        location = '/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_2_4.xlsx'
        # Reading excel file as data frame
        df = pd.read_excel(location)
        # Grouping by Dept No and Dept Name for Total Compensation
        new_df = df.groupby(["deptno", "dname"]).agg({"total_compensation": sum}).reset_index().rename(
            columns={"deptno": "Dept No", "dname": "Dept Name", "total_compensation": "Compensation"})
        # Create new xlxs and write all data into it
        new_df.to_excel("/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_4.xlsx", header=True, index=False)
        logging.info("Task 4 completed!!!")
    except Exception as e:
        logging.error(e)


def task_2_select():
    try:
        db = MyDatabase()
        # Listing the compensation
        select_pipeline = """SELECT emp.ename, jh.empno, dept.dname,dept.deptno,round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,round((enddate - startdate)/30) as emp_month_spent from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"""
        result = db.query(select_pipeline)
        logging.debug(f"Query Executed- {select_pipeline}")
        return result
    except:
        logging.error("Failed to execute the query")
    finally:
        db.close()


def task_4():
    path = "/Users/vivek/Downloads/Git-Assignment/python-sql/data/task_2_4.xlsx"
    convert_to_xlsx_for_task_2_4(task_2_select(), path)
    task_4_group_by()
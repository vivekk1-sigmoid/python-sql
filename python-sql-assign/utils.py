import logging

import pandas as pd


def convert_to_xlsx_for_task_1(data, path):
    try:
        df = pd.DataFrame(data)
        df.columns = ["Emp no", "Emp Name", "Managers"]
        df.to_excel(path, header=True, index=False)
        logging.info("Loaded to xlxs")
    except Exception as e:
        logging.error(e)


def convert_to_xlsx_for_task_2(data, path):
    try:
        df = pd.DataFrame(data)
        df.columns = ["ename","eno","dname","total_compensation","emp_month_spent"]
        df.to_excel(path, header=True, index=False)
        logging.info("Loaded to xlxs")
    except Exception as e:
        logging.error(e)


def convert_to_xlsx_for_task_2_4(data, path):
    try:
        df = pd.DataFrame(data)
        df.columns = ["ename","eno","dname","deptno","total_compensation","emp_month_spent"]
        df.to_excel(path, header=True, index=False)
        logging.info("Loaded to xlxs")
    except Exception as e:
        logging.error(e)
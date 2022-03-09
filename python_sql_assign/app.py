import logging
from task_1 import task_1
from task_2 import task_2
from task_3 import task_3
from task_4 import task_4

if __name__ == '__main__':
    logging.basicConfig(filename='/Users/vivek/Downloads/Git-Assignment/python-sql/log/system.log',
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        level=logging.DEBUG)
    # 1.Write a Python program to list employee numbers, names
    # and their managers and save in a xlsx file.
    task_1()
    # 2. Write a python program to list the Total compensation
    #  given till his/her last date or till now of all the employees till date in a xlsx file.
    task_2()
    # 3.Read and upload the above xlsx in 2) into a new table in the Postgres DB
    task_3()
    # 4.From the xlsx in 2) create another xlsx to list total compensation
    # given at Department level till date. Columns: Dept No, Dept,Name, Compensation
    task_4()
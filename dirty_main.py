from sqlalchemy import *
from application.salary import *
from application.db.people import *
import datetime as dt

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(dt.date.today())
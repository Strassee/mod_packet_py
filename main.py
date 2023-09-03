from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import date

if __name__ == '__main__':
   cs()
   ge()
   print(date.today())
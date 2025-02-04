import argparse
from datetime import datetime

__all__ = ['check_year', 'date_validator']

def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False

def check_year(year: str) -> bool:
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False

def date_validator(date: str) -> str:
    if check_year(date):
        return 'Високосный' if _check_leap_year(date) else 'Не является високосным'
    else:
        return f'Дата заполнена некорректно'

def main():
    parser = argparse.ArgumentParser(description="Проверка даты на високосность.")
    parser.add_argument("date", help="Дата в формате dd.mm.yyyy", type=str)
    args = parser.parse_args()
    print(date_validator(args.date))

if __name__ == "__main__":
    main()


# egorstolbovoj@MacBook-Pro-Egor HW_6 % python3 leap_year.py 12.01.1999
#
# Не является високосным

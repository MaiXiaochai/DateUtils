# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : example.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/6/3 16:46
------------------------------------------
使用案例
"""
from date_utils import DateUtils


def main():
    date_str = "2021-06-03 16:46:00"
    du = DateUtils()

    result = du.str_to_date(date_str)
    print(result, type(result))  # out: 2021-06-03 16:46:00 <class 'datetime.datetime'>


if __name__ == '__main__':
    main()

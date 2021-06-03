# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : date_utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/6/3 16:45
------------------------------------------
"""
from datetime import datetime, timedelta


class DateUtils:
    """
     日期处理和转换等相关功能
    """

    def __init__(self, date_format=None):
        """默认日期格式 %Y-%m-%d %H:%M:%S"""
        self.date_format = self.__trans_date_format(date_format)

    def str_to_date(self, date_str):
        """字符串转日期"""
        return datetime.strptime(date_str, self.date_format)

    def date_to_str(self, date_obj):
        """日期转字符串"""
        return date_obj.strftime(self.date_format)

    @staticmethod
    def date_offset(date_obj, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        """
            日期偏移，在给定的时间之上计算加、减一段时间后的时间，默认不偏移
        """
        offset = timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds,
                           minutes=minutes,
                           hours=hours, weeks=weeks)

        return date_obj + offset

    @staticmethod
    def diff_days(date_obj1, date_obj2) -> int:
        """
            计算两个日期相差多少天
        """
        return abs((date_obj1 - date_obj2).days)

    @staticmethod
    def __trans_date_format(date_format=None):
        return "%Y-%m-%d %H:%M:%S" if not date_format else date_format

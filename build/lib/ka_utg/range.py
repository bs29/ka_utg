# coding=utf-8
"""Koskya Utilities Module
contains the Kosakya Utilitiy Classes
"""


class Range:
    """Range Dictionary Class

    Definition:
        Range Dictionary is a Dictionary which contains the range fields:
        count, start, step
    """

    @classmethod
    def get_next(cls, dic):
        """get next suffix of range dictionary
        get next numerical or alpha suffix if start value of range
        dictionary is numeric or alpha

        Args:
            dic (dict): range dictionary
        Returns:
            list: next suffix
        """
        if dic['start'].isdigit():
            return cls.get_next_digit(dic)
        else:
            return cls.get_next_nodigit(dic)

    @staticmethod
    def get_next_digit(dic):
        """get next numerical suffix generator of range dictionary

        Args:
            dic (dict): range dictionary
        Yields:
            str: next numerical suffix
        """
        len_count = len(dic['count'])
        count = int(dic['count'])
        start = int(dic['start'])
        step = int(dic['step'])
        for ii in range(0, count):
            if ii == 0:
                next = start
            else:
                next = next + step
            len_count = len(str(next))
            fmt = '%%%ds' % len_count
            next_str = fmt % next
            yield next_str

    def get_arr(value, range_dic):
        """get array of values defined by start value and range dictionary.
        create array items by adding all next suffixes from range dictionary
        to the value.

        Args:
            value (str): start value
            range_dic (dict): range dictionary
        Returns:
            list: array of values
        """
        if range_dic:
            arr = []
            for suffix in Range.get_next(range_dic):
                value_new = f"{value}{suffix}"
                arr.append(value_new)
            return arr
        else:
            return [value]

    @classmethod
    def get_values(cls, **kwargs):
        try:
            value = kwargs.get('values')[0]
            range_dic = kwargs.get('range_dic')
            return cls.get_arr(value, range_dic)
        except Exception:
            raise

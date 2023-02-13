# coding=utf-8

from datetime import datetime

import re
import time

from .arr import Arr
from .log import Log

from ka_uts.numpy_ import UtsNumpy_

# from typing import NewType, List, Union
# AoD = NewType('AoD', List[Dict])


class GermanUmlaute:
    """ how to convert german special characters from unicode
        to utf-8 and back to unicode
    """
    d_umlaute = {
        '\xc3\xa4': 'ae',  # U+00E4	   \xc3\xa4
        '\xc3\xb6': 'oe',  # U+00F6	   \xc3\xb6
        '\xc3\xbc': 'ue',  # U+00FC	   \xc3\xbc
        '\xc3\x84': 'Ae',  # U+00C4	   \xc3\x84
        '\xc3\x96': 'Oe',  # U+00D6	   \xc3\x96
        '\xc3\x9c': 'Ue',  # U+00DC	   \xc3\x9c
        '\xc3\x9f': 'ss',  # U+00DF	   \xc3\x9f
    }

    @classmethod
    def replace(cls, s_unicode):

        for key, value in cls.d_umlaute.items():
            s_utf8 = s_unicode.encode('utf-8').replace(key, value)

        return s_utf8.decode()


class Path:

    @staticmethod
    def sh_basename(path):
        """ Extracts basename of a given path.
            Should Work with any OS Path on any OS
        """
        basename = re.search(r'[^\\/]+(?=[\\/]?$)', path)
        if basename:
            return basename.group(0)
        return path


class Int:

    @staticmethod
    def sh(s):
        try:
            ii = int(s)
            return ii
        except ValueError:
            return s


class Date:
    """ Manage Date
    """
    @staticmethod
    def to_string_xls(date):
        if date is None:
            return 'N/A'
        return time.strftime("%b-%y", date)

    @staticmethod
    def sh_today():
        return datetime.strftime(datetime.today(), '%d %m %y')

    @staticmethod
    def is_year(year):
        if year and year.isdigit():
            year_ = int(year)
            if year_ >= 1900 and year_ <= 9999:
                return True
        return False

    @classmethod
    def sh_date(cls, date_str):
        date_str = date_str.strip()
        if date_str.lower() == 'present':
            return date_str
        if cls.is_year(date_str):
            return (datetime.strptime(date_str, '%Y').strftime('%Y'))
        try:
            return (datetime.strptime(date_str, '%m %Y').strftime('%Y-%m'))
        except BaseException:
            try:
                return (datetime.strptime(date_str, '%d %m %Y').
                        strftime('%Y-%m-%d'))
            except BaseException:
                return date_str
        return date_str


class Date_Range:
    """ Manage Date Interval (Date Range)
    """
    @classmethod
    def sh_begin(cls, date_range):
        """ Show begin date
        """
        a_date_range = cls.sh_arr(date_range)
        return Date.sh_date(a_date_range[0])

    @classmethod
    def sh_end(cls, date_range):
        """ Show end date
        """
        a_date_range = cls.sh_arr(date_range)
        return Date.sh_date(a_date_range[1])

    @staticmethod
    def sh_arr(date_range):
        a_date_range = date_range.split('–')
        if len(a_date_range) == 0:
            a_date_range = ['', '']
        if len(a_date_range) == 1:
            a_date_range = a_date_range.append('')

        Log.Eq.debug("a_data_range", a_date_range)

        return a_date_range

    @staticmethod
    def set_dic(dic, date_range):
        a_date_range = date_range.split('–')
        if len(a_date_range) == 0:
            dic.start_date = ''
            dic.end_date = ''
        if len(a_date_range) == 1:
            dic.start_date = a_date_range[0].strip()
            dic.end_date = ''
        else:
            dic.start_date = a_date_range[0].strip()
            dic.end_date = a_date_range[1].strip()

        Log.Eq.debug("dic", dic)

        return dic


class Date_Range_Arr:
    """ Manage Date Interval
    """
    @staticmethod
    def get_months_between(begin_date, end_date):
        ztime = time.mktime(end_date) - time.mktime(begin_date)
        return ztime // 2592000


class Num:
    """ Manage Number
    """
    @staticmethod
    def nvl(num):
        """ nvl function similar to SQL NVL function
        """
        if num is None:
            return 0
        return num


class Numpy_:
    """ Manage Numpy Ojects
    """
    @staticmethod
    def write(prof, path_file):
        """ Write profile in numpy format
        """
        UtsNumpy_.write(path_file, prof)


class Mge:
    """ Manage Mongo DB Ojects
    """
    @staticmethod
    def write(prof, path_file):
        """ Write with Mongo engine
        """
        pass


class Soup:
    """ Manage Soup Class
    """
    @classmethod
    def traverse(cls, soup):
        dom_dic = {}
        if soup.name is None:
            return dom_dic
        dom_dic['name'] = soup.name
        arr = []
        for child in soup.children:
            if child.name is not None:
                arr.append(cls.traverse(child))
        # dom_dic.children = [cls.traverse(child)
        # for child in soup.children if child.name is not None]
        dom_dic['children'] = arr
        return dom_dic


def boolean_to_string_xls(boolean_value):
    if boolean_value is None:
        return 'N/A'
    return 'X' if boolean_value else ''


class d_Uri:
    """ Uri Management Class
    """
    @staticmethod
    def sh(d_uri, query=None):
        if query is None:
            return f"{d_uri.schema}://{d_uri.authority}{d_uri.path}"
        return f"{d_uri.schema}://{d_uri.authority}{d_uri.path}?{query}"

    @staticmethod
    def sh_path(d_uri, query=None):
        if query is None:
            return f"{d_uri.path}"
        return f"{d_uri.path}?{query}"

    @staticmethod
    def sh_authority_path(d_uri, query=None):
        if query is None:
            return f"{d_uri.authority}{d_uri.path}"
        return f"{d_uri.authority}{d_uri.path}?{query}"


class Uri:
    @staticmethod
    def verify(uri):
        uri_regex = re.compile(
          r'^(?:http|ftp)s?://'  # http:// or https://
          r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
          r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
          r'localhost|'  # localhost...
          r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
          r'(?::\d+)?'  # optional port
          r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(uri_regex, uri) is not None


class Eq:
    """ Manage Equate Class
    """
    @staticmethod
    def sh(key, value):
        """ Show Key, Value as Equate
        """
        return f"{key} = {value}"


class D_Eq:
    """ Manage Equate Dictionary Class
    """
    @staticmethod
    def sh(*args, **kwargs):
        return Arr.Eq.Dic.sh(*args, **kwargs)

    @staticmethod
    def sh_sheet_id(d_eq):
        sheet_name = d_eq.get('sheet_name')
        if sheet_name is None:
            return d_eq.get('sheet_index', 0)
        return sheet_name

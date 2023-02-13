# coding=utf-8

import re

from ka_uts.yaml import Yaml

from typing import NewType
from typing import Dict, List, Union

Value = NewType('Value', Union[str, List, Dict])


class Str:
    """ Manage String Class
    """
    def is_odd(string):
        if string.isnumeric:
            if int(string) % 2 == 0:
                return False
            return True
        else:
            return False

    def is_integer(string):
        if string[0] in ('-', '+'):
            return string[1:].isdigit()
        return string.isdigit()

    def is_boolean(string):
        if string.strip().lower() in ['true', 'false']:
            return True
        return False

    @staticmethod
    def is_undefined(string):
        """ nvl function similar to SQL NVL function
        """
        if string is None or string == '':
            return True
        return False

    @staticmethod
    def nvl(string):
        """ nvl function similar to SQL NVL function
        """
        if string is None:
            return ''
        return string

    @staticmethod
    def strip_n(string):
        """ Replace new line by Blank and strip Blanks
        """
        return string.replace('\n', ' ').strip()

    @staticmethod
    def remove(string, a_to_remove):
        """ Replace new line by Blank and strip Blanks
        """
        for to_remove in a_to_remove:
            string = string.replace(to_remove, '')
        return string

    @staticmethod
    def sh_boolean(string):
        """ Show valid Boolean string as boolean
        """
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False
        else:
            raise ValueError

    @staticmethod
    def sh_float(string):
        """ Returns Float if string is a Float
            otherwise None
        """
        try:
            num = float(string)
            return num
        except ValueError:
            return None

    @staticmethod
    def sh_arr(string):
        """ Show valid Array string as Array
        """
        # a_string = string.split(', ')
        return Yaml.safe_load(string)

    @staticmethod
    def sh_aoa(string):
        """ Show valid Array of Arrays string as Array of Arrays
        """
        len_string = len(string)
        return [re.split(string[1:len_string-1])]

    @staticmethod
    def sh_dic(string):
        """ Show valid Dictionary string as Dictionary
        """
        return Yaml.safe_load(string)

    @staticmethod
    def sh_first_item(string):
        """ Show first substring of string
        """
        return string.split()[0]

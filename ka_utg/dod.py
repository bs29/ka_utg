# coding=utf-8

from typing import NewType
from typing import Dict, List, Union

AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class DoD:
    """ Manage Dictionary of Dictionaries
    """
    @staticmethod
    def sh_value(dic, keys):
        if dic is None or keys is None or keys == []:
            return None
        if not isinstance(dic, dict):
            return None
        if isinstance(keys, str):
            keys = [keys]
        value = dic
        for key in keys:
            value = value.get(key)
            if value is None:
                return value
            if not isinstance(value, dict):
                return value
        return value

    @staticmethod
    def nvl(dod):
        """ nvl function similar to SQL NVL function
        """
        if dod is None:
            return {}
        return dod

    @classmethod
    def replace_keys(cls, d_old, keys):
        """ recurse through the dictionary while building a new one
            with new keys from a keys dictionary
        """
        d_new = {}
        for key in d_old.keys():
            key_new = keys.get(key, key)
            if isinstance(d_old[key], dict):
                d_new[key_new] = cls.replace_keys(d_old[key], keys)
            else:
                d_new[key_new] = d_old[key]
        return d_new

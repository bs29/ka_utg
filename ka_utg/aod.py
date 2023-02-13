# coding=utf-8

from .dic import Dic

from typing import NewType
from typing import Dict, List, Union

AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class AoD:
    """
    Manage Array of Dictionaries
    """
    @staticmethod
    def nvl(aod):
        """
        nvl function similar to SQL NVL function
        """
        if aod is None:
            return []
        return aod

    @staticmethod
    def sh_dod(aod, key):
        dod = {}
        for dic in aod:
            value = dic[key]
            if value not in dod:
                dod[value] = {}
            for k, v in dic.items():
                dod[value][k] = v
        return dod

    @staticmethod
    def extend_if_not_empty(aod, dic, key, function):
        if Dic.Value.is_not_empty(dic, key):
            dic = function(dic[key])
            aod.extend(dic)
        return aod

    @classmethod
    def replace_keys(cls, aod_old, keys):
        """
        recurse through the dictionary while building a new one
        with new keys from a keys dictionary
        """
        aod_new = []
        for item in aod_old:
            if isinstance(item, dict):
                item_new = Dic.replace_keys(item, keys)
                aod_new.append(item_new)
        return aod_new

    @staticmethod
    def to_doaod_by_key(aod, key):
        """
        Migrate Array of Dictionaries to Array of Key Values
        """
        doaod = {}
        if aod == []:
            return doaod
        for dic in aod:
            if key in dic:
                value = dic[key]
                if value not in doaod:
                    doaod[value] = []
                doaod[value].append(dic)
        return doaod

    @staticmethod
    def to_arr_of_key_values(aod, key):
        """
        Migrate Array of Dictionaries to Array of Key Values
        """
        arr = []
        if aod == []:
            return arr
        for dic in aod:
            for (k, v) in dic.items():
                if k == key:
                    arr.append(v)
        return arr

    @staticmethod
    def to_aoa_of_values(aod):
        """
        Migrate Array of Dictionaries to Array of Values
        """
        aoa = []
        if aod == []:
            return aoa
        for dic in aod:
            aoa.append(list(dic.values()))
        return aoa

    @staticmethod
    def sw_key_value_found(aod, key, value):
        """
        find first dictionary whose key is equal to value
        """
        for dic in aod:
            if dic[key] == value:
                return True
        return False

    @classmethod
    def to_unique_by_key(cls, aod, key):
        """
        find first dictionary whose key is equal to value
        """
        aod_new = []
        for dic in aod:
            if not cls.sw_key_value_found(aod_new, key, dic[key]):
                aod_new.append(dic)
        return aod_new

    @staticmethod
    def to_dod_by_key(iter_dic, key):
        """
        find first dictionary whose key is equal to value
        """
        dic_new = {}
        for dic in iter_dic:
            value = dic[key]
            if value in dic_new:
                msg = (f"AoD.to_dod_by_key: "
                       f"Error key: {value} "
                       f"allready exists in dic_new")
                print(msg)
            else:
                dic_new[value] = dic

    @staticmethod
    def tolc_doa_by_keys(iter_dic, key0, key1):
        dic_new = {}
        for dic in list(iter_dic):
            value0 = dic[key0].lower()
            value1 = dic[key1].lower()
            if value0 in dic_new:
                dic_new[value0].append(value1)
            else:
                dic_new[value0] = [value1]
        return dic_new

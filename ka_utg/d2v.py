# coding=utf-8

from typing import NewType
from typing import Dict, List, Union

# AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class D2V:
    @classmethod
    def sh_union(cls, d2_arr):
        arr_new = []
        for key1, key2, arr in cls.yield_values(d2_arr):
            arr_new.extend(arr)
        return arr_new

    @staticmethod
    def append(d2_v, keys, value):
        key0 = keys[0]
        key1 = keys[1]
        if key0 not in d2_v:
            d2_v[key0] = {}
        if key1 not in d2_v[key0]:
            d2_v[key0][key1] = []
        d2_v[key0][key1].append(value)
        return d2_v

    @staticmethod
    def set(d2_v, keys, value):
        key0 = keys[0]
        key1 = keys[1]
        if key0 not in d2_v:
            d2_v[key0] = {}
        d2_v[key0][key1] = value
        return d2_v

    @staticmethod
    def sh_key2values(d2_v):
        dic = {}
        for key1, d_v in d2_v.items():
            if key1 not in dic[key1]:
                dic[key1] = {}
            for key2, dummy in d_v.items():
                dic[key1].append(key2)

        return d2_v

    def yield_values(d2_v):
        for key1, d_v in d2_v.items():
            for key2, value in d_v.items():
                yield (key1, key2, value)

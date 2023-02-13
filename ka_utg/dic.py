# coding=utf-8

from .com import Com as Com

from .arr import Arr
from .obj import Obj

# from typing import NewType, Dict, List, Union
# AoD = NewType('AoD', List[Dict])


class Dic:
    """
    Manage Dictionary
    """
    @staticmethod
    def copy(dic_target, dic_source, keys=None):
        if dic_target is None:
            return
        if dic_source is None:
            return
        if keys is None:
            keys = dic_source.keys()
        for key in keys:
            dic_target[key] = dic_source[key]

    @classmethod
    def append(cls, dic, keys, value, item0=[]):
        if dic is None or keys is None or value is None:
            return
        if not isinstance(keys, (list, tuple)):
            keys = [keys]
        cls.set(dic, keys, item0)
        dic[keys[-1]].append(value)

    @classmethod
    def extend(cls, dic, keys, arr, item0=[]):
        if dic is None or keys is None or arr is None:
            return
        if not isinstance(keys, (list, tuple)):
            keys = [keys]
        cls.set(dic, keys, item0)
        dic[keys[-1]].extend(arr)

    @classmethod
    def new(cls, keys, value):
        if keys is None or value is None:
            return None
        dic = {}
        cls.set(dic, keys, value)
        return dic

    @staticmethod
    def set(dic, keys, value):
        if dic is None or keys is None or value is None:
            return
        if not isinstance(keys, (list, tuple)):
            dic[keys] = value
            return
        _dic = dic
        # all element except the last one
        for key in keys[:-1]:
            if key not in _dic:
                _dic[key] = {}
            _dic = _dic[key]
        # last element
        _dic[keys[-1]] = value

    @staticmethod
    def increment(dic, keys, item0=1):
        if dic is None:
            return
        if keys is None:
            return

        if not isinstance(keys, (list, tuple)):
            keys = [keys]

        dic_ = dic

        # all element except the last one
        for key in keys[:-1]:
            if key not in dic_:
                dic_[key] = {}
            dic_ = dic_[key]

        # last element
        key = keys[-1]

        if key not in dic_:
            dic_[key] = item0
        else:
            dic_[key] += 1

    @staticmethod
    def lstrip_keys(dic, str):
        dic_new = {}
        for k, v in dic.items():
            k_new = k.replace(str, "", 1)
            dic_new[k_new] = v
        return dic_new

    @staticmethod
    def is_not(dic, key):
        if key in dic:
            not dic[key]
        else:
            return None

    @staticmethod
    def nvl(dic):
        """ nvl function similar to SQL NVL function
        """
        if dic is None:
            return {}
        return dic

    @staticmethod
    def sh_prefixed(dic, prefix):
        dic_new = {}
        for key in dic:
            dic_new[f"{prefix}_{key}"] = dic[key]
        return dic_new

    @staticmethod
    def sh_union(doa):
        arr_new = []
        for key, arr in doa.items():
            arr_new.extend(arr)
        return arr_new

    @staticmethod
    def sh_value2keys(dic):
        dic_new = {}
        for key, value in dic.items():
            if value not in dic_new:
                dic_new[value] = []
            if key not in dic_new[value]:
                dic_new[value].extend(key)
        return dic_new

    class Names:

        @staticmethod
        def sh(d_data, key='value'):
            try:
                names = Obj.extract_values(d_data, key)
            except Exception as e:
                Com.Log.error(e, exc_info=True)
                names = []
            finally:
                return names

        @classmethod
        def sh_item0(cls, d_names):
            names = cls.sh(d_names)
            return Arr.sh_item0(names)

        @classmethod
        def sh_item0_if(cls, string, d_names):
            names = cls.sh(d_names)
            return Arr.sh_item0_if(string, names)

    class Key:

        @staticmethod
        def change(dic, source_key, target_key):
            if source_key in dic:
                dic[target_key] = dic.pop(source_key)
            return dic

    class Value:

        @staticmethod
        def get(dic, keys, default=None):
            if keys is None:
                return dic
            if len(keys) == 0:
                return dic

            value = dic
            for key in keys:
                if key not in value:
                    return default
                value = value[key]
                if value is None:
                    break
            return value

        @classmethod
        def set(cls, dic, keys, value):
            if value is None:
                return
            if dic is None:
                return
            if keys is None:
                return

            if not isinstance(keys, (list, tuple)):
                keys = [keys]

            value_curr = cls.get(dic, keys[:-1])
            if value_curr is None:
                return
            last_key = keys[-1]
            if last_key in value_curr:
                value_curr[last_key] = value

        @classmethod
        def is_empty(cls, dic, keys):
            if dic is None:
                return True
            if isinstance(keys, str):
                keys = [keys]
            if isinstance(keys, (list, tuple)):
                value_curr = cls.get(dic, keys)
                if value_curr is None:
                    return True
                if isinstance(value_curr, str):
                    if value_curr == '':
                        return True
                elif isinstance(value_curr, (list, tuple)):
                    if value_curr == {}:
                        return True
            return False

        @classmethod
        def is_not_empty(cls, dic, keys):
            return not cls.is_empty(dic, keys)

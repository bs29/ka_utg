# coding=utf-8

from ka_uts.json import Json

from typing import NewType
from typing import Dict, List, Union

AoD = NewType('AoD', List[Dict])
Value = NewType('Value', Union[str, List, Dict])


class Obj:
    """ Manage Object
    """
    @staticmethod
    def shrink_array(obj):
        if isinstance(obj, (tuple, list)):
            if len(obj) == 1:
                return obj[0]
        return obj

    @classmethod
    def verify_key_type(cls, obj, sw=True, type=(str)):
        if obj is None:
            return sw
        for item in obj:
            if isinstance(item, dict):
                for key in item.keys():
                    if not isinstance(key, type):
                        sw = False
                        print(f"key: {key} is not of type: {type}")
                        print(f"key type of key: {key} is {type(key)}")
                for value in item.values():
                    if not cls.verify_key_type(value, sw, type):
                        return False
        return sw

    @classmethod
    def verify_key_type_str(cls, obj, sw=True):
        return cls.verify_key_type(obj, sw, type=(str))

    @staticmethod
    def yield_aod(obj):
        """ show objects as Array of Dictionaries
        """
        if isinstance(obj, (list, tuple)):
            for _obj in obj:
                yield _obj
        elif isinstance(obj, (dict, str)):
            yield obj

    @staticmethod
    def sh_aod(obj, fncs=None):
        """ show objects as Array of Dictionaries
        """
        aod = []
        if fncs is None:
            if isinstance(obj, (list, tuple)):
                for _obj in obj:
                    aod.append(_obj)
            elif isinstance(obj, (dict, str)):
                aod.append(obj)
            return aod

        if isinstance(obj, (list, tuple)):
            for _obj in obj:
                obj_new = fncs(_obj)
                if obj_new is not None:
                    if isinstance(obj_new, (dict, str)):
                        if obj_new != {}:
                            aod.append(obj_new)

        elif isinstance(obj, dict):
            obj_new = fncs(obj)
            if obj_new is not None:
                if isinstance(obj_new, (dict, str)):
                    if obj_new != {}:
                        aod.append(obj_new)

        return aod

    @staticmethod
    def sh_arr(obj):
        if obj is None:
            return obj
        if isinstance(obj, (list, tuple)):
            return obj
        else:
            return [obj]

    @staticmethod
    def to_string(obj, separator='.'):
        if obj is None:
            return ''
        elif isinstance(obj, (list, tuple)):
            return separator.join(obj)
        elif isinstance(obj, str):
            return obj.strip()
        elif isinstance(obj, int):
            return str(obj)
        else:
            return ''

    @staticmethod
    def sh_text(obj):
        if isinstance(obj, (list, tuple)):
            return ' '.join(obj)
        else:
            return obj

    @classmethod
    def flatten(cls, obj):
        array = []
        for element in obj:
            if isinstance(element, list):
                array.extend(cls.flatten(element))
            else:
                array.append(element)
        return array

    @classmethod
    def extract_values(cls, obj, key, **kwargs):
        arr = kwargs.get('arr', [])
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    cls.extract_values(v, key, arr=arr)
                if k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                cls.extract_values(item, key, arr=arr)
        return arr

    class Json:

        @classmethod
        def write(obj, path_, **kwargs):
            sw_verify = kwargs.get('sw_orjson', False)
            if sw_verify:
                if not Obj.verify_key_type_str(obj):
                    # print(f'fuck:path_ = {path_}')
                    return
            Json.write(obj, path_, **kwargs)

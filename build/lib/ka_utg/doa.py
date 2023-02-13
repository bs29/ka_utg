# coding=utf-8

from .arr import Arr

# from typing import NewType, Dict, List, Tuple, Union, Any
# T_Arr = NewType('T_Arr', Union[List, Tuple])
# T_DoDA = NewType('T_DoDA', Dict[T_DA])
# T_DA = NewType('T_DA', Union[Dict, T_Arr])
# T_SLT = NewType('T_SLT', Union[str, List, Tuple])
# T_SLTD = NewType('T_SLTD', Union[str, List, Tuple, Dict])


class DoA:
    """
    Manage Dictionary of Array
    """
    @staticmethod
    def apply(arr_function, doa, keys, item, item0=[]):
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return
        _doa = doa
        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]
        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0
        _doa[key].append(item)
        arr_function(_doa[key], item)

    @staticmethod
    def append(doa, keys, item, item0=[]):
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return
        _doa = doa
        # all keys elements except the last
        # if len(keys) > 1:
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]
        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0
        _doa[key].append(item)

    @staticmethod
    def append_unique(doa, keys, item, item0=[]):
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return
        _doa = doa
        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]
        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0
        Arr.append_unique(_doa[key], item)

    @staticmethod
    def extend(doa, keys, item):
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        if not isinstance(keys, (list, tuple)):
            return
        _doa = doa

        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]

        # last keys element
        key = keys[-1]
        if isinstance(item, str):
            item = [item]
        if key not in _doa:
            _doa[key] = item
        else:
            _doa[key].extend(item)

    @staticmethod
    def set(doa, keys, item0=[]):
        """
        assign item to dictionary defined as value
        for the given keys.
        """
        if isinstance(keys, str):
            keys = [keys]
        elif not isinstance(keys, (list, tuple)):
            return
        _doa = doa
        # all keys elements except the last
        for key in keys[:-1]:
            if key not in _doa:
                _doa[key] = {}
            _doa = _doa[key]
        # last keys element
        key = keys[-1]
        if key not in _doa:
            _doa[key] = item0

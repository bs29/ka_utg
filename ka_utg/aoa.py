# coding=utf-8

# from .log import Log
# from .dic import Dic
from .arr import Arr

from typing import NewType
from typing import Dict, List, Union

Value = NewType('Value', Union[str, List, Dict])


class AoA:
    """ Manage Array of Arrays
    """
    @staticmethod
    def nvl(aoa):
        """ nvl function similar to SQL NVL function
        """
        if aoa is None:
            return []
        return aoa

    @staticmethod
    def to_aod(aoa, keys):
        """ Migrate Array of Arrays to Array of Dictionaries
        """
        arr = []
        aod = []
        for arr in aoa:
            dic = Arr.to_dic(arr, keys)
            aod.append(dic)
        return aod

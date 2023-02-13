# coding=utf-8

from typing import NewType
from typing import Dict, List, Union

Value = NewType('Value', Union[str, List, Dict])


class AoO:
    """ Manage Array of Objects
    """
    @staticmethod
    def to_unique(aoo):
        """ Removes duplicates from Array of Objects
        """
        aoo_new = []
        for ee in aoo:
            if ee not in aoo_new and ee is not None:
                aoo_new.append(ee)
        return aoo_new

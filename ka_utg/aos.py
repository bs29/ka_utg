# coding=utf-8

from typing import NewType, List
T_AoS = NewType('T_AoS', List[str])


class AoS:
    """ Manage Array of Strings
    """

    @staticmethod
    def nvl(aos: T_AoS) -> T_AoS:
        """ nvl function similar to SQL NVL function
        """
        if aos is None:
            return []
        return aos

    @staticmethod
    def to_lower(aos: T_AoS) -> T_AoS:
        """ Lower all elements of the array of strings
        """
        return [element.lower() for element in aos]

    class Unique:
        """ unique Array of Strings
        """

        @staticmethod
        def to(aos: T_AoS) -> T_AoS:
            """ Removes duplicate items from a list
            """
            aos_new = []
            for ee in aos:
                if ee not in aos_new:
                    aos_new.append(ee)
            return aos_new

        @staticmethod
        def to_lower(aos: T_AoS) -> T_AoS:
            ''' Removes duplicate lower items from a list
            '''
            aos_new_lower = []
            for ee in aos:
                ee_lower = ee.lower()
                if ee_lower not in aos_new_lower:
                    aos_new_lower.append(ee_lower)
            return aos_new_lower

        @staticmethod
        def to_lower_invariant(arr: T_AoS) -> T_AoS:
            """ Removes duplicate items (case invariant) from a list
            """
            arr_new = []
            arr_new_lower = []
            for ee in arr:
                ee_lower = ee.lower()
                if ee_lower not in arr_new_lower:
                    arr_new_lower.append(ee_lower)
                    arr_new.append(ee)
            return arr_new

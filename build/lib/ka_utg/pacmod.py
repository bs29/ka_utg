# coding=utf-8

import os
import pkg_resources

from typing import Dict


class Pacmod:
    """ Package Module Management
    """
    def init(package: str, module: str) -> Dict:
        """ init Pacmod Dictionary
        """
        pacmod = {}
        pacmod[package] = package
        pacmod[module] = module
        return pacmod

    class Cfg:
        """ Configuration Sub Class of Package Module Class
        """
        @staticmethod
        def sh_path(pacmod: Dict) -> str:
            """ show directory
            """
            package = pacmod['package']
            module = pacmod['module']
            dir = f"{package}.data"
            return pkg_resources.resource_filename(dir, f"{module}.yml")

    class Pmd:
        """ Package Sub Class of Package Module Class
        """
        @staticmethod
        def sh_path_keys(pacmod: Dict, filename: str = 'keys.yml') -> str:
            """ show directory
            """
            package = pacmod.package
            dir = f"{package}.data"
            return pkg_resources.resource_filename(dir, filename)

    class Path:
        class Data:
            class Dir:
                """ Data Directory Sub Class
                """
                @staticmethod
                def sh(pacmod: Dict, type: str) -> str:
                    """ show Data File Path
                    """
                    package = pacmod.package
                    module = pacmod.module
                    return f"/data/{package}/{module}/{type}"

        @classmethod
        def sh(
                cls, pacmod: Dict,
                type: str,
                suffix: str,
                pid,
                ts,
                **kwargs) -> str:
            """ show type specific path
            """
            filename = kwargs.get('filename')
            if filename is not None:
                filename_ = filename
            else:
                filename_ = type

            sw_filename_pid_ts = kwargs.get('sw_filename_pid_ts', True)
            if sw_filename_pid_ts is None:
                sw_filename_pid_ts = True

            dir = cls.Data.Dir.sh(pacmod, type)
            if sw_filename_pid_ts:
                # pid = str(Com.pid)
                # ts = str(Com.ts_start)
                file_path = os.path.join(
                              dir, f"{filename_}_{pid}_{ts}.{suffix}")
            else:
                file_path = os.path.join(dir, f"{filename_}.{suffix}")
            return file_path

        @classmethod
        def sh_pattern(
                cls,
                pacmod: Dict,
                type: str,
                suffix: str, **kwargs) -> str:
            """ show type specific path
            """
            filename = kwargs.get('filename')
            dir = cls.Data.Dir.sh(pacmod, type)
            return os.path.join(dir, f"{filename}*.{suffix}")

        class Log:

            @staticmethod
            def sh_cfg(
                  pacmod={'package': 'ka_utg', 'module': 'com'},
                  filename='log.yml'):
                """ show directory
                """
                return pkg_resources.resource_filename(
                         f"{pacmod['package']}.data", filename)

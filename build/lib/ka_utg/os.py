# coding=utf-8
"""Koskya Utilities Module
contains the Kosakya Utilitiy Classes
"""

import distro


class OS:

    OS2os_dist = {
        'suse': 'sles',
        'centos': 'rhel',
        'rhel': 'rhel',
        'oracle': 'rhel',
        'ubuntu': 'ubuntu'
    }

    @classmethod
    def get_os_dist(cls):
        try:
            os_details = distro.linux_distribution(
                           full_distribution_name=False)
            os = os_details[0]
            return cls.OS2os_dist.get(os, None)
        except Exception as e:
            # KaLog.stop(exc=e)
            raise e

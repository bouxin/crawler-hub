#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubo
# @since 2020-10-04
#
from hub.util.http_client import get, get_proxy


def random_proxy():
    """
    custom proxy http:port
    :return: http:port
    """
    _dict = get_proxy()

    if _dict.get('code') == 200:
        return _dict.get('data').get('proxy')


if __name__ == '__main__':
    print(random_proxy())

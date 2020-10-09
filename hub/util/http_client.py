#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubo
# @since 2020-10-09
#
import requests
from logging import getLogger
import ast
from hub import settings


def get_proxy():
    return get('proxy')


def get(url):
    try:
        result = requests.request(url=settings.PROXY if url == 'proxy' else url, method='GET')

        if result and result.status_code == 200:
            response = {
                'code': 200,
                'message': 'Success',
                'data': ast.literal_eval(result.text)
            }
        else:
            response = {
                'code': result.status_code,
                'message': result.reason
            }
    except RuntimeError as error:
        getLogger().info(error)
        response = {
            'code': 500,
            'message': 'Service Error!'
        }
    return response

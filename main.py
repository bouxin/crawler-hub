#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubo
# @since 2020-10-02
# @description app main
from scrapy.cmdline import execute


def get_spiders():
    # todo import all hub.spiders@*_spider.py
    return ['demo']


def get_all_spiders():
    spiders = ['scrapy', 'crawl']
    for elem in get_spiders():
        spiders.append(elem)
    return spiders


if __name__ == '__main__':
    # global import spiders
    execute(get_all_spiders())

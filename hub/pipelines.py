#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubo
# @since 2020-10-02
# @description --

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from item adapter import ItemAdapter


class DemoPipeline:
    def process_item(self, item, spider):
        return item

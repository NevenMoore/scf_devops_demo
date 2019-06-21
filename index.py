# -*- coding: utf8 -*-
import flask


def main_handler(event, context):
    print(str(event))
    return "hello world"


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Automatically generated by Generator
# Date: {{ date|date }}

if __name__ == '__main__':
    list = [ {% for task in tasks %} '{{task}}', {%endfor%} ]
    print [ task.upper() for task in list ]

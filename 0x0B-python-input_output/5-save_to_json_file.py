#!/usr/bin/python3
"""Module description for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """returns the json representation of an object"""
    m_json = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(m_json)

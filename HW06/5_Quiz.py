"""
5. Написать программу, которая откроет файл (questions.json) и после ответов на вопросы, запишет их назад 
в этот же файл.
"""

import json
from pprint import pprint

FILE_CONTENT = {}


def read_file(file_path):
    global FILE_CONTENT
    with open(file_path) as file:
        FILE_CONTENT = json.load(file)


def change_answer1():
    global FILE_CONTENT
    answ = input(f"{FILE_CONTENT['quiz']['q1']['question']} ")
    FILE_CONTENT['quiz']['q1']['answer'] = answ


def change_answer2():
    global FILE_CONTENT
    answ = input(f"{FILE_CONTENT['quiz']['q2']['question']} ")
    FILE_CONTENT['quiz']['q2']['answer'] = answ


def change_answer3():
    global FILE_CONTENT
    answ = input(f"{FILE_CONTENT['quiz']['q3']['question']} ")
    FILE_CONTENT['quiz']['q3']['answer'] = answ


def save_data(file_path):
    global FILE_CONTENT
    with open(file_path, 'w') as file:
        json.dump(FILE_CONTENT, file, indent=4)


read_file('questions.json')
change_answer1()
change_answer2()
change_answer3()
pprint(FILE_CONTENT, indent=4)

save_data('questions.json')


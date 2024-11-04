#!/usr/bin/env python

import os

def start():
    os.system('poetry install')
    os.system('poetry run jupyter lab')

if __name__ == "__main__":
    start()

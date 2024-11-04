#!/usr/bin/env python

import os

def scrub():
    os.system('poetry run -- jupyter nbconvert --clear-output --inplace *.ipynb') 

if __name__ == "__main__":
    scrub()

#!/usr/bin/env python

import os
import subprocess

BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))

os.environ['PYTHONPATH'] = os.path.join(BASE_PATH, os.pardir, "src")
subprocess.run('mkdocs serve', shell=True)

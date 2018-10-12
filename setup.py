# encoding: UTF-8

"""
Augustus - An event-driven algorithm trading library in Python.

This Project is an open source quantitative trading framework written in Python.
"""

import os

from setuptools import Command,find_packages,setup

class CleanCommand(Command):
    user_options=[]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.egg-info")

setup(
    name="Augustus",
    version="0.0.1",
    author="Jialue Chen",
    authoremail="jialuechen@outlook.com",
    license="MIT",
    url="https://github.com/jialuechen/augustus",
    description="Algorithm trading framework in Python",
    packages=find_packages(),
    cmdClass={
        "clean":CleanCommand,
    },install_requires=["pandas","numpy","pymongo"]
)
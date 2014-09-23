#runs the setup for py2exe to package the program and its dependencies, to run it you need to install py2exe.

from distutils.core import setup
import py2exe

setup(console=['main.py'])

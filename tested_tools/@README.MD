# This directory contains all the tested tools of any programming language like python, html, js, css

## each tools is in a separate file. and also each python function is in a separate file.

## This folder can be used as a python package by following two method -

1. select the script you need and create your own package (see python notes to know how to do this)
2. copy this folder and paste to your project and at the top of your main script add

`import sys, os
sys.path.insert(1, os.path.realpath(os.path.join(__file__, "..", "tested_tools")))`

Note: THERE IS ONLY ONE SYS.PATH PER INTERPRETER PROCESS, AND BOTH THE MAIN SCRIPT AND ALL IMPORTED MODULES SEE THE SAME SYS.PATH OBJECT.

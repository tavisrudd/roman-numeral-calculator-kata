#!/bin/bash

while true; do
    inotifywait -e modify roman/tests/test_calculator.py
    nosetests 
done

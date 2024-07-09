# Imports go at the top
from microbit import *
from whaley_sans_font import show_number, test_font


test_font()

# Code in a 'while True:' loop repeats forever
while True:
    show_number(temperature())
    sleep(1000)
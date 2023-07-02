"""
File: check08.py
Author: Brother Burton

Purpose: Practice using for loops.
"""

# 1. Iterate through a list of items
colors = ["red", "blue", "green", "yellow"]

for color in colors:
    print(color)

print() # A blank line to make the output look nicer

# 2. Iterate through a list of numbers
for i in range(1, 99):
    print(i)

print() # A blank line to make the output look nicer

# 3. Iterate through even numbers

# Notice that we start at 4, go up through, but not including 288, and count by 4
for i in range(4, 288, 4):
    print(i)
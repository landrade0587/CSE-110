"""
File: check11.txt
Author: Luis Andrade
Date: 3 december 2022
Purpose: Prove Assignment Milestone.
"""
with open("life-expectancy.csv") as  book_file:
   
   for line in  book_file:
        book = line.strip()
        print(book)




   

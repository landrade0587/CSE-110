"""
File: teach11.py
Author: Luis Andrade
Date: 03 december 2022
Purpose: Practice working with files.
"""

with open("hr_system.txt") as f:
   
   for line in f:
        clean_line = line.strip()
        parts = clean_line.split(" ")
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])  
        pay_amount = salary / 24

        if title.lower() == "Scientist":
            pay_amount += 1000

        print(f"{name} ----(ID: {id_number})---- {[title]} ---- ${pay_amount:.2f}")
"""
Maggie Cloos
11-18-2020
Agile UNO Module 7
"""

# 1
# import my_module & pprint
import my_module

import pprint

# 2
# use the greeting method from my_module to print out your name
name = "Maggie"

print(my_module.greeting(name))

# 3
# use the letter_text module to print out a string
print(my_module.letter_text(name = "Maggie", amount = "10", denomination = "dollars"))

# 4
# use the my_module.my_json_data and print it out
from my_module import my_json_data

print(my_json_data)

# 5
# import the my_json_data as my_data and print out the my_json_data using pprint
from my_module import my_json_data as my_data

pprint.pprint(my_data)

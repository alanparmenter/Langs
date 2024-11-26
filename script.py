import os
import sys
from langs import langs
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
letter_choice = ''
while not letter_choice.isalpha() or len(letter_choice) != 1 or letter_choice != letter_choice.upper():
    letter_choice = input("Please enter an upper case letter then press return: ")
lang_list = [lang['language'] for lang in langs[letter_choice]]
print(f"Search results: {lang_list}")
attribute_choice_prompt = """Please enter a number then press return for a recommendation maximising:
1) difficulty
2) popularity
3) recency
Input: """
attribute_choice = 0
while not 1 <= int(attribute_choice) <= 3:
    attribute_choice = input(attribute_choice_prompt)
    try:
        int(attribute_choice)
    except ValueError:
        attribute_choice = 0
        continue
choices = ['null', 'difficulty', 'popularity', 'recency']
choice = choices[int(attribute_choice)]
choice_lambda = lambda x: x[choice]
recommendation = max(langs[letter_choice], key=choice_lambda)
print(f"Recommendation: {recommendation['language']}")
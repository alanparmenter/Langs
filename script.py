from langs import langs
letter_choice = input("Please enter an upper case letter then press return: ")
lang_list = [lang['language'] for lang in langs[letter_choice]]
print(f"Search results: {lang_list}")
attribute_choice = input(
"""Please enter a number then press return for a recommendation maximising:
1) difficulty
2) popularity
3) recency
Input: """
)
choices = ['null', 'difficulty', 'popularity', 'recency']
choice = choices[int(attribute_choice)]
choice_lambda = lambda x: x[choice]
recommendation = max(langs[letter_choice], key=choice_lambda)
print(f"Recommendation: {recommendation['language']}")
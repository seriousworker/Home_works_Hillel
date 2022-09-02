"""
Дана строка (большАя строка, лучше взять на английском). Выведите слово, которое в этой строке встречается чаще всего. Если таких слов несколько, выведите последнее.

Задачу необходимо решить с использованием словаря.

"""


given_string1 = 'Big black bug bit a big black dog on his big black nose'
given_string2 = 'But good morning Good morning to ye and thou I’d say to all my patients because I was the worse of the hypocrites of all the hypocrites the cruel and phony hypocrites I was the very worst'
given_string3 = 'Nory was a Catholic because her mother was a Catholic and Nory’s mother was a Catholic because her father was a Catholic and her father was a Catholic because his mother was a Catholic or had been'


def get_most_repeated_word(got_string: str) -> str:
    to_str = [word.lower() for word in got_string.split()]
    words_dict = {word: to_str.count(word) for word in to_str}
    res_list = [key for key, value in words_dict.items() if value == max(words_dict.values())]
    return res_list[-1]


print(get_most_repeated_word(given_string1))
print(get_most_repeated_word(given_string2))
print(get_most_repeated_word(given_string3))

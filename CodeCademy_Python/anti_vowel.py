import re

def anti_vowel(t):
    vowels = ['a', 'e', 'i', 'o', 'u']
    t_list = list(t)
    n_list = []
    for e in t_list:
        if e.lower() not in vowels:
            n_list.append(e)
    n_list = ''.join(n_list)
    return n_list

def anti_vowel_regex(t):
    return re.sub('[aeiou]', '', t, flags=re.I) if t else ""

def filter_vowel(t):
    def vowels(l):
        if l.lower() not in  ['a', 'e', 'i', 'o', 'u']:
            return l
    return filter(vowels, t)

text = "Hey look Words!"
print anti_vowel(text)
print anti_vowel_regex(text)
print filter_vowel(text)
def censor(string, word):
    string = string.split()
    bad_words = ['hack', 'fuck', 'hey', 'wack']
    new_string = []
    for e in string:
        if e.lower() not in bad_words:
            new_string.append(e)
        else:
            wordlen =  len(str(e))
            new_string.append("*" * wordlen)
    censored = " ".join(new_string)
    return censored
    
print censor("hey this hack is wack hack", "hack") 
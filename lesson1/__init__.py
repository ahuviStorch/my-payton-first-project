def isPolidrom(string):
    while len(string) > 1:
        if string[0] != string[-1]:
            return False
        else:
            string = string[1:-1]
    return True


print(isPolidrom("rtyfdytr"))


def countWords(string):
    counter = 1
    for i in range(len(string)):
        if string[i] == " ":
            counter += 1
    return counter


print(countWords("gsjkn jhim fnmo k"))


def acronyms(string):
    strNew = ""
    if string[0] != " ":
        strNew = string[0]
    for i in range(len(string)):
        if string[i] == " ":
            if len(string) > i + 1:
                strNew += string[i + 1]
    return strNew
print(acronyms("ahuvi storch .  yhudit"))
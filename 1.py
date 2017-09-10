import string

def run():
    s = raw_input('enter a string: ')
    print challenge1(s)

def challenge1(sentence):
    result = ''
    lowercase_list = list(string.ascii_lowercase)[::-1]
    for i in list(sentence):
        if i.islower():
            theIndex = lowercase_list.index(i)
            i = lowercase_list[25-theIndex]
        result += i
    return result

if __name__ == '__main__':
    run()

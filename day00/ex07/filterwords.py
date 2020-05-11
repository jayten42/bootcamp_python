import sys
import string
if __name__ == '__main__':
    string = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    if string.isnumeric():
        quit("ERROR")
    try:
        n = int(sys.argv[2])
    except ValueError:
        quit("ERROR")
    lst = [word for word in  string.split() if word.isalnum() and len(word) > n]
    print(lst)
import time


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is  mandatory"""
    if not isinstance(text, str):
        yield "ERROR"
        return
    words = text.split(sep)
    if option is not None and option not in ["shuffle", "unique", "ordered"]:
        yield "ERROR"
        return
    if option == "shuffle":
        shuffled = []
        while words:
            idx = int(time.time()) % len(words)
            shuffled.append(words.pop(idx))
        words = shuffled
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words = sorted(words, key=str.swapcase)
    for word in words:
        yield word


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print("\nshuffled:")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("\nordered:")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("\nunique:")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
def text_analyzer(text=""):
    if text == "":
        text = input("What is the text to analyse?\n")
    count_total = len(text)
    count_upper_case = sum([x.isupper() for x in text])
    count_lower_case = sum([x.islower() for x in text])
    count_space = sum([x.isspace() for x in text])
    count_punctuation = count_total - count_upper_case - count_lower_case - count_space - sum([x.isdigit() for x in text])
    print("The text contains {} characters:\n".format(count_total))
    print("{} upper letters\n".format(count_upper_case))
    print("{} lower letters\n".format(count_lower_case))
    print("{} punctuation letters\n".format(count_punctuation))
    print("{} spaces letters\n".format(count_space))

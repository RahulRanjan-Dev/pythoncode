def translate(text):
    vowels = "aeiou"
    result = ""
    prev_char = ""

    for char in text:
        if char in vowels and prev_char not in vowels:
            result += "av" + char
            #print(result)
        else:
            result += char
        prev_char = char

    return result


text='langue de feu'
res=translate(text)
print(res)
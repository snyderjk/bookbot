def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    for letter in text.lower():
        if letter in result:
            result[letter] +=1
        else:
            result[letter] = 1

    return sort_dict(result)

def sort_on(items):
    return items["num"]


def sort_dict(dict):
    result = []
    for ch in dict:
        count = dict[ch]
        result.append({ "char": ch, "num": count})

    result.sort(reverse=True, key=sort_on)
    return result
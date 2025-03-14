def count_words(text):
    return f"{len(text.split())}"
def count_chars(text):
    text = text.lower()
    chars = {}
    for char in text:
        if f"{char}" in chars.keys():
            chars[f'{char}'] += 1
        else:
            chars[f'{char}'] = 1
    return chars

def sort_dict(chars_str):
    dict = count_chars(chars_str)
    dict = sorted(dict.items(), reverse=True, key=lambda char: char[1])
    return dict
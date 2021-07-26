from string import ascii_lowercase, ascii_uppercase, ascii_letters

def caesar_shift(value, key):
    if value in ascii_lowercase:
        corresponding_index = (ascii_lowercase.index(value) + key) % 26
        return ascii_lowercase[corresponding_index]
    else:
        corresponding_index = (ascii_uppercase.index(value) + key) % 26
        return ascii_uppercase[corresponding_index]

def rot13(code):
    result = ""
    for i in code:
        if i not in ascii_letters:
            result += i
        else:
            result += caesar_shift(i, 13)
    return result

def main():
    code = "Hello world!"
    result = rot13(code)
    print(result)

if __name__ == "__main__":
    main()
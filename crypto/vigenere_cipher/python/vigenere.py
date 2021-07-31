import string


class VigenereTable(object):
    def __init__(self, range: list) -> None:
        self.range = range
        self.first_char = range[0]

    def get_element(self, row: str, col: str) -> str:
        index = (ord(row) - ord(self.first_char)) + (ord(col) - ord(self.first_char))
        return self.range[index % len(self.range)]

    def get_col(self, row: str, element: str) -> str:
        index = (ord(element) - ord(self.first_char)) - (ord(row) - ord(self.first_char))
        return self.range[index % len(self.range)]


class Vigenere(object):
    def __init__(self) -> None:
        self.upper_table = VigenereTable(string.ascii_uppercase)
        self.lower_table = VigenereTable(string.ascii_lowercase)

    def encode(self, plaintext: str, key: str) -> str:
        result = ""
        valid_char_counter = 0
        for char in plaintext:
            if char not in string.ascii_letters:
                result += char
                continue
            if char in string.ascii_uppercase:
                result += self.upper_table.get_element(row=key[valid_char_counter % len(key)], col=char)
            if char in string.ascii_lowercase:
                result += self.lower_table.get_element(row=key[valid_char_counter % len(key)], col=char)
            valid_char_counter += 1
        return result

    def decode(self, cipher: str, key: str) -> str:
        result = ""
        valid_char_counter = 0
        for char in cipher:
            if char not in string.ascii_letters:
                result += char
                continue
            if char in string.ascii_uppercase:
                result += self.upper_table.get_col(row=key[valid_char_counter % len(key)], element=char)
            if char in string.ascii_lowercase:
                result += self.lower_table.get_col(row=key[valid_char_counter % len(key)], element=char)
            valid_char_counter += 1
        return result

    def find_key(self, cipher: str, partial_plaintext: str) -> str:
        result = ""
        for c, p in zip(cipher, partial_plaintext):
            if c not in string.ascii_letters:
                continue
            if p not in string.ascii_letters:
                result += "?"
                continue
            if c in string.ascii_uppercase:
                result += self.upper_table.get_col(row=p.upper(), element=c)
            if c in string.ascii_lowercase:
                result += self.lower_table.get_col(row=p.lower(), element=c)
        return result


if __name__ == "__main__":
    vigenere = Vigenere()
    print(vigenere.encode(plaintext="hello world!", key="heiyou"))
    print(vigenere.decode(cipher="oitjc qvvtb!", key="heiyou"))
    print(vigenere.find_key(cipher="oitjc qvvtb!", partial_plaintext=".ello wo"))

# Vigenere cipher
## Description
Vigenere cipher is based on Caesar cipher. First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later. This earned it the description le chiffre indéchiffrable. (From wikipedia, https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
To encode or decode, we need to have the KEY.
We can use the table to help encode or decode. ![vigenere table](./image/Vigenère_square_shading.png)

## Process
1. We need to have a key.
2. For a given plain text, we need to extend the key to the same length as the plain text (ignore whitespaces and punctuation).
3. So the each character in plain text has a corresponding letter from the key, using the Vigenere table to determine the encoded letter. 

* Example:
1. Key: LEARN
2. Plain text: HelloWorld
3. Extend the key: LEARNLEARN
4. the first letter in the key is "L", find the line "L" in the table, then search for the column "H" which is the first letter of the plain text, so the first character in the cipher text is "S". The second, letter in the key is "E", and the second letter in plain text is "e", find the line "E" with colunm "E", which gives "i" in lower case. and so on.
5. the final cipher is "SilcbHsrcq".
punctuation = '!#$%&*+-=?@^_., '


def decryption(txt, lang, stp):
    res = ''
    if lang == 1:
        for c in txt:
            if c in punctuation:
                res += c
            else:
                if 1040 <= ord(c) <= 1071:
                    decript = ord(c) - stp
                    if decript < 1040:
                        crypt = 1072 - (1040 - decript)
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) - stp))
                elif 1072 <= ord(c) <= 1103:
                    decript = ord(c) - stp
                    if decript < 1072:
                        crypt = 1104 - (1072 - decript)
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) - stp))
    if lang == 2:
        for c in txt:
            if c in punctuation:
                res += c
            else:
                if 97 <= ord(c) <= 122:
                    decript = ord(c) - stp
                    if decript < 97:
                        crypt = 123 - (97 - decript)
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) - stp))
                elif 65 <= ord(c) <= 90:
                    decript = ord(c) - stp
                    if decript < 65:
                        crypt = 91 - (65 - decript)
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) - stp))
    print(res)


def incryption(txt, lang, stp):
    res = ''
    if lang == 1:
        for c in txt:
            if c in punctuation:
                res += c
            else:
                if 1040 <= ord(c) <= 1071:
                    decript = ord(c) + stp
                    if decript > 1071:
                        crypt = 1039 + stp - (1071 - ord(c))
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) + stp))
                elif 1072 <= ord(c) <= 1103:
                    decript = ord(c) + stp
                    if decript > 1103:
                        crypt = 1071 + stp - (1103 - ord(c))
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) + stp))
    if lang == 2:
        for c in txt:
            if c in punctuation:
                res += c
            else:
                if 65 <= ord(c) <= 90:
                    decript = ord(c) + stp
                    if decript > 90:
                        crypt = 64 + (90 - ord(c)) - stp
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) + stp))
                elif 97 <= ord(c) <= 122:
                    decript = ord(c) + stp
                    if decript > 122:
                        crypt = 96 + stp - (122 - ord(c))
                        res += str(chr(crypt))
                    else:
                        res += str(chr(ord(c) + stp))
    print(res)


operation = int(input('направление: 1 - шифрование; 2 - дешифрование - '))
language = int(input('язык алфавита: 1 - русский; 2 - английский - '))
step = int(input('шаг сдвига (со сдвигом вправо для шифрования и влево для дешифровки) - '))
message = input('Ваше сообщение: ')
print('Шифр: ', end ='')
if operation == 1:
    incryption(message, language, step)
elif operation == 2:
    decryption(message, language, step)
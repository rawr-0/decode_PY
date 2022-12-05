def decode(s, shift):
    f2.write(f"{shift};")
    for i in s:
        t = False
        if 1072 > ord(i) > 1040:
            i = chr(ord(i) + 32)
            t = True
        if i != "." and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and \
                i != "8" and i != "9" and i != "0" and i != " " and i != "-" and i != "\n" and i != 'ё':
            if ord(i) - shift > 1103:
                if t:
                    f2.write(chr(1072 + ((ord(i) - shift) - 1104) - 32))
                else:
                    f2.write(chr(1072 + ((ord(i) - shift) - 1104)))
            else:
                if ord(i) - shift < 1072:
                    if t:
                        f2.write(chr(1103 - (1071 - (ord(i) - shift)) - 32))
                    else:
                        f2.write(chr(1103 - (1071 - (ord(i) - shift))))
                else:
                    if t:
                        f2.write(chr(ord(i) - shift - 32))
                    else:
                        f2.write(chr(ord(i) - shift))
        else:
            f2.write(i)


if __name__ == '__main__':
    f = open("student_address.txt", "r", encoding="utf-8")
    f2 = open("decoded.txt", "w", encoding="utf-8")
    while True:
        file_line = f.readline()
        if not file_line:
            print("End Of File")
            break
        q = len(file_line) - 1
        while file_line[q] != '.':
            q -= 1
        shift = ord(file_line[q - 1]) - ord('в')
        decode(file_line, shift)

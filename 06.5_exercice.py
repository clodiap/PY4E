text = "X-DSPAM-Confidence:    0.8475"
at_position = text.find(":")
# print(at_position)

number = text[at_position+1 : ]
# print(number)

snumber = number.lstrip()
# print(snumber)

fnumber = float(snumber)
print(fnumber)

print("\n\n\n NEW\n")

str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(":")
# print(ipos)
piece = str[ipos+2:]
# print(piece)
value = float(piece)
print(value)
# print(value + 42.0)

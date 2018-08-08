#  7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

filename = input("Enter a filename: ")

fhand = open("mbox-short.txt")

count = 0
total = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    else:
        count += 1
        number = line[line.find(":")+1 :]
        snumber = number.strip()
        # fnumber = float(snumber)
        total = float(total) + float(snumber)

moyenne = float(total) / float(count)
print("Average spam confidence:", moyenne)
# print(round(moyenne , 12))





quit()

count = 0
totalnumber = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        count += 1
        atpos = line.find(":")
        number = float(line[atpos+1:])
        # fnumber = float(number)
        totalnumber += number

print(totalnumber)

print(count)

xaverage = totalnumber / float(count)
print("Average spam confidence:", xaverage)


print("\n\n\n NEW\n")

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fh = open("mbox-short.txt")
comptage = 0
grandtotal = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    comptage += 1
    pos_deuxpoints = line.find(":")
    nombre = line[pos_deuxpoints+1:]
    nombre = nombre.rstrip()
    print("nombre",float(nombre))
    grandtotal = grandtotal + float(nombre)
    print("grandtotal", grandtotal, "nombre", nombre, "comptage", comptage)
    moyenne = grandtotal / float(comptage)
    print("moyenne:",moyenne)


print(grandtotal / comptage)

import time


def findPal(bplength):
    f = open("dna.txt", 'r')
    f2 = open("dnaResults.txt", 'w')
    strand = f.read()
    loc = []
    counter = 0
    for num in range(0, len(strand) - 1):
        check = strand[num: num + bplength]
        if check == invComplement(check):
            f2.write(check + "\n")
            loc.append(num)
            counter += 1
    f.close()
    f2.close()
    return loc


def invComplement(str):
    str = str[::-1]
    newStr = ''
    for char in str:
        if char == 'a':
            newStr += 't'
        elif char == 't':
            newStr += 'a'
        elif char == 'g':
            newStr += 'c'
        elif char == 'c':
            newStr += 'g'
    return newStr


def main():
    bplength = int(input("What length do you want for palindrome? \n"))
    start = time.time()
    results = findPal(bplength)
    end = time.time()
    total = end - start
    print(results)
    print(len(results))
    print(total)


main()
#punnett square with 2 genes
import re
def dipunsquare(a, b, c, d, e, f, g, h):
    gene1 = a + b + c + d
    print("organism 1: " + gene1)
    gene2 = e + f + g + h
    print("organism 2: " + gene2)

    dipun1 = a + c
    dipun2 = a + d
    dipun3 = b + c
    dipun4 = b + d

    dipun5 = e + g
    dipun6 = e + h
    dipun7 = f + g
    dipun8 = f + h

    gene1var = [dipun1, dipun2, dipun3, dipun4]
    gene2var = [dipun5, dipun6, dipun7, dipun8]
    print("organism 1 gametes:")
    print(gene1var)
    print("organism 2 gametes:")
    print(gene2var)

    dichild = []
    pattern = re.compile('[A-Z]')
    al1 = pattern.match(a)
    if al1:
        allele1 = 1
    else:
        allele1 = 0
    al2 = pattern.match(c)
    if al2:
        allele2 = 1
    else:
        allele2 = 0
    al3 = pattern.match(b)
    if al3:
        allele3 = 1
    else:
        allele3 = 0
    al4 = pattern.match(d)
    if al4:
        allele4 = 1
    else:
        allele4 = 0
    if allele1 == 1:
        if allele2 == 1:
            dichild.append(a+e+c+g)
            dichild.append(a+e+c+h)
            dichild.append(a+f+c+g)
            dichild.append(a+f+c+h)
            dipun11 = a+e+c+g
            dipun12 = a+e+c+h
            dipun13 = a+f+c+g
            dipun14 = a+f+c+h

        else:
            dichild.append(a+e+g+c)
            dichild.append(a+e+h+c)
            dichild.append(a+f+g+c)
            dichild.append(a+f+h+c)
            dipun11 = a+e+g+c
            dipun12 = a+e+h+c
            dipun13 = a+f+g+c
            dipun14 = a+f+h+c

    else:
        if allele2 == 1:
            dichild.append(e+a+c+g)
            dichild.append(e+a+c+h)
            dichild.append(f+a+c+g)
            dichild.append(f+a+c+h)
            dipun11 = e+a+c+g
            dipun12 = e+a+c+h
            dipun13 = f+a+c+g
            dipun14 = f+a+c+h

        else:
            dichild.append(e+a+g+c)
            dichild.append(e+a+h+c)
            dichild.append(f+a+g+c)
            dichild.append(f+a+h+c)
            dipun11 = e+a+g+c
            dipun12 = e+a+h+c
            dipun13 = f+a+g+c
            dipun14 = f+a+h+c

    #dipun2 time
    if allele1 == 1:
        if allele4 == 1:
            dichild.append(a+e+d+g)
            dichild.append(a+e+d+h)
            dichild.append(a+f+d+g)
            dichild.append(a+f+d+h)
            dipun21 = a+e+d+g
            dipun22 = a+e+d+h
            dipun23 = a+f+d+g
            dipun24 = a+f+d+h
        else:
            dichild.append(a+e+g+d)
            dichild.append(a+e+h+d)
            dichild.append(a+f+g+d)
            dichild.append(a+f+h+d)
            dipun21 = a+e+g+d
            dipun22 = a+e+h+d
            dipun23 = a+f+g+d
            dipun24 = a+f+h+d

    else:
        if allele4 == 1:
            dichild.append(e+a+d+g)
            dichild.append(e+a+d+h)
            dichild.append(f+a+d+g)
            dichild.append(f+a+d+h)
            dipun21 = e+a+d+g
            dipun22 = e+a+d+h
            dipun23 = f+a+d+g
            dipun24 = f+a+d+h

        else:
            dichild.append(e+a+g+d)
            dichild.append(e+a+h+d)
            dichild.append(f+a+g+d)
            dichild.append(f+a+h+d)
            dipun21 = e+a+g+d
            dipun22 = e+a+h+d
            dipun23 = f+a+g+d
            dipun24 = f+a+h+d

    #dipun3 time
    if allele3 == 1:
        if allele2 == 0:
            dichild.append(b+e+c+g)
            dichild.append(b+e+c+h)
            dichild.append(b+f+c+g)
            dichild.append(b+f+c+h)
            dipun31 = b+e+c+g
            dipun32 = b+e+c+h
            dipun33 = b+f+c+g
            dipun34 = b+f+c+h

        else:
            dichild.append(b+e+g+c)
            dichild.append(b+e+h+c)
            dichild.append(b+f+g+c)
            dichild.append(b+f+h+c)
            dipun31 = b+e+g+c
            dipun32 = b+e+h+c
            dipun33 = b+f+g+c
            dipun34 = b+f+h+c

    else:
        if allele2 == 1:
            dichild.append(e+b+c+g)
            dichild.append(e+b+c+h)
            dichild.append(f+b+c+g)
            dichild.append(f+b+c+h)
            dipun31 = e+b+c+g
            dipun32 = e+b+c+h
            dipun33 = f+b+c+g
            dipun34 = f+b+c+h

        else:
            dichild.append(e+b+g+c)
            dichild.append(e+b+h+c)
            dichild.append(f+b+g+c)
            dichild.append(f+b+h+c)
            dipun31 = e+b+g+c
            dipun32 = e+b+h+c
            dipun33 = f+b+g+c
            dipun34 = f+b+h+c

    #dipun4 time
    if allele3 == 1:
        if allele4 == 1:
            dichild.append(b+e+d+g)
            dichild.append(b+e+d+h)
            dichild.append(b+f+d+g)
            dichild.append(b+f+d+h)
            dipun41 = b+e+d+g
            dipun42 = b+e+d+h
            dipun43 = b+f+d+g
            dipun44 = b+f+d+h

        else:
            dichild.append(b+e+g+d)
            dichild.append(b+e+h+d)
            dichild.append(b+f+g+d)
            dichild.append(b+f+h+d)
            dipun41 = b+e+g+d
            dipun42 = b+e+h+d
            dipun43 = b+f+g+d
            dipun44 = b+f+h+d

    else:
        if allele4 == 1:
            dichild.append(e+b+d+g)
            dichild.append(e+b+d+h)
            dichild.append(f+b+d+g)
            dichild.append(f+b+d+h)
            dipun41 = e+b+d+g
            dipun42 = e+b+d+h
            dipun43 = f+b+d+g
            dipun44 = f+b+d+h

        else:
            dichild.append(e+b+g+d)
            dichild.append(e+b+h+d)
            dichild.append(f+b+g+d)
            dichild.append(f+b+h+d)
            dipun41 = e+b+g+d
            dipun42 = e+b+h+d
            dipun43 = f+b+g+d
            dipun44 = f+b+h+d

    #print(dichild1)
    #print(dichild2)
    #print(dichild3)
    #print(dichild4)

    print(dichild)

    newset = set([dipun11,dipun12,dipun13,dipun14, dipun21, dipun22, dipun23, dipun24, dipun31, dipun32, dipun33, dipun34, dipun41, dipun42, dipun43, dipun44])
    print("unique combinations:")
    print(newset)
    indexset = []
    for i in newset:
       indexset.append(i)
    #print(list1)
    print("Amount of unique combinations ",int(len(indexset)))
    response = input("Do you want to find allele frequencies? [y/n]")
    while response != "n":
        if response == "y":
            which = int(input("Choose which unique combo # you want to find (1, 2, 3, 4, etc.)"))
            if which <= len(indexset):
                print("Allele frequency for",indexset[which-1])
                print(dichild.count(indexset[which-1])/len(dichild))
                response = input("Do you want to find allele frequencies? [y/n]")
            else:
                print("Please enter a value between 1 and", int(len(indexset)))
        elif response == "n":
            exit
        else:
            print("Please enter a valid value, y or n:")
            response = input()
        
        

input1 = input("gene 1's first allele ")
input2 = input("gene 1's second allele ")
input3 = input("gene 1's third allele ")
input4 = input("gene 1's fourth allele ")
input5 = input("gene 2's first allele ")
input6 = input("gene 2's second allele ")
input7 = input("gene 3's third allele ")
input8 = input("gene 4's fourth allele ")
dipunsquare(input1, input2, input3, input4, input5, input6, input7, input8)

repeat = input("do you want to do another punnet square? [y/n] ")
while repeat != 'n':
    if repeat == "y":
        input1 = input("gene 1's first allele ")
        input2 = input("gene 1's second allele ")
        input3 = input("gene 1's third allele ")
        input4 = input("gene 1's fourth allele ")
        input5 = input("gene 2's first allele ")
        input6 = input("gene 2's second allele ")
        input7 = input("gene 3's third allele ")
        input8 = input("gene 4's fourth allele ")
        dipunsquare(input1, input2, input3, input4, input5, input6, input7, input8)
        repeat = input("do you want to do another punnet square? [y/n] ")
    elif repeat == "n":
        exit
    else:
        print("Please enter a valid value, y or n:")
        repeat = input()

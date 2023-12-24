prmd_mass = []                      # буквы, из которых состоит каждая пирамида
invert_prmd = []                    # позиции неперевернутых пирамид

def positions_invert_prmd(str):     # расчет позиций, где находятся перевернутые пирамиды
    position = 3
    invert_prmd.append(position)
    n = 1
    for i in range(int(len(str))):
        position += 3               # при переходе между строками номера перевернутых пирамид отличаются на 3 позиции
        invert_prmd.append(position)
        for i in range(n):
            position += 2           # при переходе в рамках одной строки номера перевернутых пирамид отличаются на 3 позиции
            invert_prmd.append(position)
        n += 1

def prmd_init(str):
    prmd_mass.append(str[0:4])
    prmd_count = 1                  # номер пирамиды
    elem_count = 3                  # номер буквы
    n = 3
    for i in range(3, int(len(str) / 4), n):
        if(elem_count < int(len(str) / 4)):
            for j in range(n):
                prmd_count += 1
                elem_count += 1
                if(prmd_count not in invert_prmd):          # если пирамида неперевернутая, заносится в массив ее вершина
                    prmd_mass.append(str[elem_count])
                else:
                    prmd_mass.append(str[elem_count:elem_count + 3])      # если пирамида перевернутая, заносится в массив ее сторона
                    elem_count += 2
            prmd_count -= n
            for j in range(n):
                prmd_count += 1
                elem_count += 1
                if (prmd_count not in invert_prmd):             # аналогично со второй половиной пирамиды
                    prmd_mass[prmd_count - 1] += str[elem_count:elem_count + 3] # сначала заносятся стороны неперевернутых
                    elem_count += 2
                else:
                    prmd_mass[prmd_count - 1] += str[elem_count]                # потом вершины перевернутых
            n += 2

def ident_elem_check():                                         # сжатие маленьких пирамид
    for i in range(len(prmd_mass)):
        ident_elem_number = 1
        for j in range(len(prmd_mass[i])):
            if (j != 3):
                if (prmd_mass[i][j] == prmd_mass[i][j + 1]):
                    ident_elem_number += 1
        if (ident_elem_number == 4):
            prmd_mass[i] = prmd_mass[i][0]


with open("input.txt", "r") as file:
    str = file.read()
str = str[::-1]
positions_invert_prmd(str)
prmd_init(str)
ident_elem_check()
res_str = ""
for i in range(len(prmd_mass)):
    res_str += prmd_mass[i]
res_str = res_str[::-1]
with open("output.txt", "w") as file:
    file.write(res_str)


"""
Во втором примере, где:
    input.txt
    aaaaaaabcccccccaaaaabbbcccccaaabbbbbcccabbbbbbbcdddddddddddddddd
    output.txt
    abcd
не происходит сжатие средних пирамид, поскольку сжимаются только средние пирамиды с буквой d, но при этом пирамида принимает
неправильную форму.

Возможно, рисунок в файле вместе со всеми заданиями наглядно объяснит вышеизложенное
"""

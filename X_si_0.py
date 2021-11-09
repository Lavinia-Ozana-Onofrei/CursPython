tabla = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_tabla():
    print(' {0}|{1}|{2}\n {3}|{4}|{5}\n {6}|{7}|{8}'.format(str(tabla[0]), str(tabla[1]), str(tabla[2]),
                                                            str(tabla[3]), str(tabla[4]), str(tabla[5]),
                                                            str(tabla[6]), str(tabla[7]), str(tabla[8])))


winner = ' '
cnt = 9
while cnt:
    player = int(input("Alege o pozitie: "))

    if player not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Pozitie incorecta")
        continue
    if tabla[player - 1] == ' ':
        tabla[player - 1] = 'X'
    else:
        print("Alege alta pozitie")
        continue

    cnt -= 1
    print_tabla()

    if cnt < 6:
        for i in [0, 1, 2]:
            if tabla[i] == tabla[i + 3] == tabla[i + 6] and tabla[i] != ' ':
                winner = tabla[i]
                break
        for i in [0, 3, 6]:
            if tabla[i] == tabla[i + 1] == tabla[i + 2] and tabla[i] != ' ':
                winner = tabla[i]
                break
        if (tabla[0] == tabla[4] == tabla[8]) or \
                (tabla[2] == tabla[4] == tabla[6]) and tabla[4] != ' ':
            winner = tabla[4]
        if winner == 'X':
            print("Felicitari!Ai castigat!")
            break
        elif winner == 'O':
            print(" Ai pierdut!")
            break

    position = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for i in position:
        if tabla[i - 1] == ' ':
            tabla[i - 1] = 'O'
            print("Computerul a ales: {0}".format(i))
            cnt -= 1
            break

    print_tabla()

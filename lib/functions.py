def printDicc (dicc):
    for i in dicc:
        print(f'Verice: {i}')
        for j in dicc[i]:
            print(f'\tRel: {j} \n\t\t peso:{dicc[i][j]}')
    return 0
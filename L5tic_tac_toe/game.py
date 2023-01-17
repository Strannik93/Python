def create_matrix():
    matrix = [['*' for _ in range(3)], ['*' for _ in range(3)], ['*' for _ in range(3)]]
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(*matrix[i], sep=' ')

def step(matrix):
    while True:
        try:
            line = int(input('Введите номер строки(сверху вниз от 1 до 3): '))
            row = int(input('Введите номер столбца(слева направо от 1 до 3): '))
            if 0 < line < 4 and 0 < row < 4 and matrix[line-1][row-1] == '*':
                return line-1, row-1
            elif 0 < line < 4 and 0 < row < 4: print('Место уже занято!')
            else: print('Такая позиция не существует!')
        except:
            print('Номер строки и столбца должны быть целыми!')

def check_steps(matrix,player,name_player):
    steps = control(matrix,player)
    if steps == False: 
        print(f'{name_player} победил')
        return steps
    else:
        steps = control_free_steps(matrix)
        if steps == False: print('Ничья')
        return steps

def control_free_steps(matrix):
    check = False
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if matrix[i][k] == '*':
                check = True
                return check
    return check

def control(matrix, player):
    check = True
    count = 0
    for i in range(len(matrix)):
        if matrix[i][i] == player: count += 1
    if count == 3: 
        check = False
        return check
    count = 0
    for i in range(len(matrix)):
        if matrix[i][len(matrix)-i-1] == player: count += 1
    if count == 3:
        check = False
        return check
    for i in range(len(matrix)):
        count = 0
        for k in range(len(matrix[i])):
            if matrix[i][k] == player: count += 1
        if count == 3: 
            check = False
            return check
    for k in range(len(matrix[0])):
        count = 0
        for i in range(len(matrix)):
            if matrix[i][k] == player: count += 1
        if count == 3: 
            check = False
            return check
    return check

def check_free_slot(matrix,coord,player):
    check = False
    count = 0
    for i in range(len(coord)):
        line, row = coord[i]
        if matrix[line][row] == player: count += 1
    if count == 2:
        for i in range(len(coord)):
            line, row = coord[i]
            if matrix[line][row] == '*': return line, row
    return check

def check_player(matrix, player):
    check = False
    coord = ['' for _ in range(len(matrix))]
    for i in range(len(matrix)):
        coord[i] = (i,i)
    check = check_free_slot(matrix,coord,player)
    if type(check) == tuple: return check
    for i in range(len(matrix)):
        coord[i] = (i,len(matrix)-i-1)
    check = check_free_slot(matrix,coord,player)
    if type(check) == tuple: return check
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            coord[k] = (i,k)
        check = check_free_slot(matrix,coord,player)
        if type(check) == tuple: return check
    for k in range(len(matrix[0])):
        for i in range(len(matrix)):
            coord[i] = (i,k)
        check = check_free_slot(matrix,coord,player)
        if type(check) == tuple: return check
    return check

def bot_step(matrix,player):
    if player == 'X': opponent = 'O'
    else: opponent = 'X'
    if matrix[1][1] == '*': return 1, 1
    check = check_player(matrix,player)
    if type(check) == tuple: return check
    check = check_player(matrix,opponent)
    if type(check) == tuple: return check
    if matrix[1][1] == matrix[0][0] == player:
        if matrix[0][1] == matrix[0][len(matrix)-1] == matrix[len(matrix)-1][1] == '*': return 0, 1
        elif matrix[1][0] == matrix[len(matrix)-1][0] == matrix[1][len(matrix)-1] == '*': return 1, 0
    elif matrix[1][1] == matrix[0][len(matrix)-1] == player:
        if matrix[1][len(matrix)-1] == matrix[len(matrix)-1][len(matrix)-1] == matrix[1][0] == '*':
            return 1, len(matrix)-1
        elif matrix[0][1] == matrix[0][0] == matrix[len(matrix)-1][1] == '*': return 0, 1
    elif matrix[1][1] == matrix[len(matrix)-1][len(matrix)-1] == player:
        if matrix[1][len(matrix)-1] == matrix[0][len(matrix)-1] == matrix[1][0] == '*':
            return 1, len(matrix)-1
        elif matrix[len(matrix)-1][1] == matrix[len(matrix)-1][0] == matrix[0][1] == '*':
            return len(matrix)-1, 1
    elif matrix[1][1] == matrix[len(matrix)-1][0] == player:
        if matrix[1][0] == matrix[0][0] == matrix[1][len(matrix)-1] == '*':
            return 1, 0
        elif matrix[len(matrix)-1][1] == matrix[len(matrix)-1][len(matrix)-1] == matrix[0][1] == '*':
            return len(matrix)-1, 1
    if player == 'X':
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if matrix[i][k] == opponent:
                    if i > 0 and k > 0 and matrix[0][0] == '*': return 0, 0
                    elif i > 0 and k < len(matrix[i])-1 and matrix[0][len(matrix[i])-1] == '*':
                        return 0, len(matrix[i])-1
                    elif i < len(matrix)-1 and k < len(matrix[i])-1 and matrix[len(matrix)-1][len(matrix[i])-1] == '*':
                        return len(matrix)-1, len(matrix[i])-1
                    elif i < len(matrix)-1 and k > 0 and matrix[len(matrix)-1][0] == '*':
                        return len(matrix)-1, 0
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if matrix[i][k] == '*': return i, k
    else:
        if matrix[1][1] == opponent:
            if matrix[0][0] == '*': return 0, 0
            elif matrix[0][len(matrix)-1] == '*': return 0, len(matrix)-1
            elif matrix[len(matrix)-1][len(matrix)-1] == '*':
                return len(matrix)-1, len(matrix)-1
            elif matrix[len(matrix)-1][0] == '*': return len(matrix)-1, 0
            for i in range(len(matrix)):
                for k in range(len(matrix[i])):
                    if matrix[i][k] == '*': return i, k
        else:
            if matrix[len(matrix)-1][len(matrix)-1] == opponent: 
                if matrix[0][0] == '*': return 0, 0
                elif matrix[len(matrix)-2][len(matrix)-1] == '*':
                    return len(matrix)-2, len(matrix)-1
                elif matrix[len(matrix)-1][len(matrix)-2] == '*':
                    return len(matrix)-1, len(matrix)-2
            elif matrix[len(matrix)-1][0] == opponent:
                if matrix[0][len(matrix)-1] == '*': return 0, len(matrix)-1
                elif [len(matrix)-2][0] == '*': return len(matrix)-2, 0
                elif matrix[len(matrix)-1][1] == '*': return len(matrix)-1, 1
            elif matrix[0][0] == opponent:
                if matrix[len(matrix)-1][len(matrix)-1] == '*': return len(matrix)-1, len(matrix)-1
                elif matrix[1][0] == '*': return 1, 0
                elif matrix[0][1] == '*': return 0, 1
            elif matrix[0][len(matrix)-1] == opponent: 
                if matrix[len(matrix)-1][0] == '*': return len(matrix)-1, 0
                elif matrix[1][len(matrix)-1] == '*': return 1, len(matrix)-1
                elif matrix[0][len(matrix)-2] == '*': return 0, len(matrix)-2
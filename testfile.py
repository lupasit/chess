import matrix as mt
chessField = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']
        ]
def printBoard():
    for row in chessField:
        print(''.join(row))
def move(startPos:str,endPos:str,board:list[list])->list[list]:
    #Принимаем строки
    # получаем срезы
    startColStr = startPos[:1]
    startRowStr = startPos[1:]
    endColStr = endPos[:1]
    endRowStr = endPos[1:]
    # из типа str в тип int (для строк)
    startRowInt= int(startRowStr) - 1
    endRowInt= int(endRowStr) - 1
    #для столбцов
    # A - 0 B - 1 C - 2 D - 3 E - 4 F - 5 G - 6 H - 7
    col = ['A','B','C','D','E','F','G','H']
    # проверка на наличие, индекс и есть номер столбца
    if startColStr.upper() in col:
        startColInt = col.index(startColStr.upper())
        # print(startColInt)
    else:
        print("ти ебень")
    if endColStr.upper() in col:
        endColInt = col.index(endColStr.upper())
    else:
         print("ти ебеньx2")
    # 00 - начальное положение по строкам 10 - начальное по столбцам
    # для конечного точно так же
    startMoveVector = [
        [startRowInt],
        [startColInt]
        ]
    endMoveVector = [
        [endRowInt],
        [endColInt]
    ]
    # получаем какой фигурой ходим
    figure:str = board[startRowInt][startColInt]
    return startMoveVector,endMoveVector,figure
def movePawn(startPos:str,endPos:str,board:list[list]=chessField):
    startMoveVector,endMoveVector,figure = move(startPos,endPos,board)
    if (board[startMoveVector[0][0]][startMoveVector[1][0]] == 'p') and ((mt.subM(startMoveVector,endMoveVector) == [[-1],[0]]) or (mt.subM(startMoveVector,endMoveVector) == [[1],[0]])) :
        board[startMoveVector[0][0]][startMoveVector[1][0]] = '.'
        board[startMoveVector[0][0]+1][startMoveVector[1][0]] = 'p'
        printBoard()
    elif (board[startMoveVector[0][0]][startMoveVector[1][0]] == 'P') and ((mt.subM(startMoveVector,endMoveVector) == [[-1],[0]]) or (mt.subM(startMoveVector,endMoveVector) == [[1],[0]])) :
        board[startMoveVector[0][0]][startMoveVector[1][0]] = '.'
        board[startMoveVector[0][0]-1][startMoveVector[1][0]] = 'P'
        printBoard()
def moveRook(startPos:str,endPos:str,board:list[list]=chessField):
    # startMoveVector - sMV,endMoveVector - eMV
    sMV,eMV,figure = move(startPos,endPos,board)
    # endMoveVectorMax for Rook = eMVM
    eMVM = [
        [8],
        [8]
    ]
    # if (figure == "r"):
    #     mt.print_mat(eMVM)
    # else:
    #     print("zxc")


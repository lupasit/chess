import matrix as mt
# from testfile import chessField
# from testfile import move

A = [
    [1],
    [1]
]
B = [
    [8],
    [1]
]
# сходил прямо
C = [
    [0],
    [8]
]
Max = [
    [8],
    [8]
]
v = [
    [-1],
    [-1]
]
v1 = [
    [-1],
    [1]
]
# posRow != -1
# else
# testBoard = [
#     ['p','.'],
#     ['.','P'],
#     ['.','.']
# ]
# c точки startMoveVector[0][0]+1(or startMoveVector[1][0]+)
# пройтись до точки endMoveVector[0][0](or endMoveVector[1][0])
# и проверить каждую клетку на отличие от '.'
# def check(startPos,endPos,board=chessField):
#     startMoveVector,endMoveVector,figure = move(startPos,endPos,board)
#     distrow = abs(startMoveVector[0][0] -endMoveVector[0][0])
#     distcol = abs(startMoveVector[0][1]-endMoveVector[0][1])
#     if distrow > distcol:
#         for i in range(startMoveVector[0][0],distrow):
#             if board[i][startMoveVector[1][0]] != '.':
#                return False
#     else:
#         for i in range(startMoveVector[1][0],distcol):
#
#             if board[startMoveVector[0][0]][i] != '.':
#                 return False
#     return True
# ошибка в логике
#
#
# сходил в бок
# mt.print_mat(mt.absMatrix(mt.subM(A,B)))
# print(Max[0][0] >= mt.absMatrix(mt.subM(A,B))[0][0])
# из testfile это проверка на перемещение по строкам
# Max[1][0] >= mt.absMatrix(mt.subM(A,B))[1][0]
# Это бессмысленно, но пусть будет (проверка на ход по столбцам)
# True - по правилам может сходить
# с board[startMoveVector[0][0]][startMoveVector[1][0]]
# удалить фигуру и поставить "."
# на board[endMoveVector[0][0]][endMoveVector[1][0]]
# поставить фигуру при условии, что на пути не было никаких фигур
# надо написать функцию проверки прямой по row, col и по диагонали
# в moveRook будет проверяться есть ли на пути фигуры(белые, черные)
# при условии того что фигура будет противоположного цвета то
# либо берем(при endMoveVector[0][0] or endMoveVector[1][0]
# что в этих точках будет находиться энеми фигура)
# либо ходит до eMV[0][0] eMV[1][0] так же при условии
# того что по прямой (startMoveVector[0][0], endMoveVector[0][0])
# (или [1][0]) будут только "."
# но надо проверить работу при проверке sMV[0][0] eMV[0][0]
# с sMV eMV
# бля да я в ахуе че я написал
# пешки теперь могут брать фигуры
# осталось функцию проверки диагонали от 1 -ой точки до 2 -ой и прямых
# for i in range(0+1,2):
#     print(i)
# прописать надо range(startMoveVector[0][0]+1,endMoveVector[0][0])
# для col так же только [1][0]
# должно сработать пока хз




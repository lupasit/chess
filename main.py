import matrix as mt
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

# сходил в бок
mt.print_mat(mt.absMatrix(mt.subM(A,B)))
print(Max >= mt.absMatrix(mt.subM(A,B)))
# True - по правилам может сходить
# с board[startMoveVector[0][0]][startMoveVector[1][0]]
# удалить фигуру и поставить "."
# на board[endMoveVector[0][0]][endMoveVector[1][0]]
# поставить фигуру при условии, что на пути не было никаких фигур

# 1 => black
# 0 => white
# I should return a new matrix without the ones that are neither on the matrix's edges nor connected, 
# horizontally or vertically, to their ones.
# Example:
# [                        [
#  [1, 0, 0, 0, 0, 0],      [1, 0, 0, 0, 0, 0],
#  [0, 1, 0, 1, 1, 1],      [0, 0, 0, 1, 1, 1],
#  [0, 0, 1, 0, 1, 0],  =>  [0, 0, 0, 0, 1, 0],
#  [1, 1, 0, 0, 1, 0],      [1, 1, 0, 0, 1, 0],
#  [1, 0, 1, 1, 0, 0],      [1, 0, 0, 0, 0, 0],
#  [1, 0, 0, 0, 0, 1]       [1, 0, 0, 0, 0, 1]
# ]                        ]

def removeIslands(matrix):
    # For checking: matrix[4][2]'s close chunks are matrix[3][2], matrix[5][2], matrix[4][1] and matrix[4][3]
    def checkNearby(elementX, elementY):
        elementList = []
        directions = {'elementUp': (elementX - 1, elementY), 'elementDown': (elementX + 1, elementY), 'elementLeft': (elementX, elementY - 1), 'elementRight': (elementX, elementY + 1)}
        for d in directions:
            try:
                if matrix[directions[d][0]][directions[d][1]] == 1: elementList.append((directions[d][0], directions[d][1]))
            except:
                continue
        return elementList
    
    # Write a matrix with the exact same size and full of zeroes
    newMatrix = []
    for i in matrix:
        temp = []
        for j in matrix:
            temp.append(0)
        newMatrix.append(temp)

    continents = {}
    matrixSize = len(matrix)
    for i in list(range(matrixSize)):
        if matrix[0][i] == 1: continents[(0, i)] = True
        if matrix[matrixSize - 1][i] == 1: continents[(matrixSize - 1, i)] = True
        if i < matrixSize and i > 0:
            if matrix[i][0] == 1: continents[(i, 0)] = True
            if matrix[i][matrixSize - 1] == 1: continents[(i, matrixSize - 1)] = True
    
    def writeContinents():
        continentRest = {}
        for c in continents:
            posContinents = checkNearby(c[0], c[1])
            if len(posContinents) > 0:
                for i in posContinents:
                    continentRest[(i[0], i[1])] = True
        for r in continentRest: 
            continents[(r[0], r[1])] = True

    continentsSize = len(continents)
    writeContinents()
    while len(continents) > continentsSize: 
        continentsSize = len(continents)
        writeContinents()
        
    for c in continents:
        newMatrix[c[0]][c[1]] = 1
    
    return newMatrix

print(removeIslands([[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]]))
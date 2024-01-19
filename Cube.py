# Luiz Gabriel Figueiredo de Carvalho (15/01/2024)

# This code will serve to transform a json containing the cube info to an object
# which contains two other objects, to organize all that is needed to solve the cube.

import json

class PieceFace:

    def __init__ (self, color, axis, direction):
        self.color = color #string
        self.axis = axis #char
        self.direction = direction #char

    def changePieceFace (self, newAxis, newDirection):
        self.axis = newAxis
        self.direction = newDirection

class Piece:

    def __init__ (self, position, file):
        self.position = position
        facesCounter = 0

        direction = 0
        if (position[0] != 0): # x axis
            facesCounter += 1

            direction = getDirection(position[0])
            
            self.xPiece = PieceFace(file[direction+'x'][-position[1]+1][position[0]*position[2]+1],'x', position[0])
        else:
            self.xPiece = None
        
        if (position[1] != 0): # y axis
            facesCounter += 1

            direction = getDirection(position[1])
            
            self.yPiece = PieceFace(file[direction+'y'][position[1]*position[0]+1][position[2]+1],'y', position[1])
        else:
            self.yPiece = None

        if (position[2] != 0): # z axis
            facesCounter += 1

            direction = getDirection(position[2])
            
            self.zPiece = PieceFace(file[direction+'z'][-position[1]+1][-position[2]*position[0]+1],'z', position[2])
        else:
            self.zPiece = None

        if facesCounter == 1:
            self.type = "center"
        elif facesCounter == 2:
            self.type = "middle"
        elif facesCounter == 3:
            self.type = "corner"
        else:
            self.type = "cubeCenter"

        #print(self.type)
        #if (self.xPiece != None):
        #    print(self.xPiece.color, end=" ")
        #if (self.yPiece != None):
        #    print(self.yPiece.color, end=" ")
        #if (self.zPiece != None):
        #    print(self.zPiece.color, end=" ")
        #print(position)
        #print(" ")

    def changePiece (self, newPosition, newAxis):
        self.position = newPosition

class Cube:

    def __init__ (self, file):
        value = 0
        self.pieces = [[[value for z in range(3)] for y in range(3)] for x in range(3)]

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.pieces[x][y][z] = Piece((x-1, y-1, z-1), file)
                #print(' ')
            #print("----------")

def readFile (file):
    with open (file) as cube:
        return json.load(cube)

def createCube (file):
    cubeFile = readFile(file)

    cube = Cube(cubeFile)

    return cube

def rotateFace (cube, face, direction):
    direction
    
def getDirection (direction):
    if direction < 0:
        return '-'
    else:
        return '+'
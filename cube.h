#ifndef _CUBE_H_
#define _CUBE_H_

#define X 1
#define Y 1
#define Z 1
#define CENTER 0

#define x 0
#define y 1
#define z 2

#define WHITE 0
#define BLUE 1
#define RED 2
#define GREEN 3
#define ORANGE 4
#define YELLOW 5

typedef struct {
    int position[3];
    int color[3];
    char type[7]; 
} Piece;

typedef struct {
    Piece face[9];
} Face;

typedef struct {
    Face cubeUnsolved[6];
    Face cubeSolved[6];
} Cube;

Piece* readPiece ();

Face* readFace ();

Cube* readCube ();

#endif
#include <iostream>
#include <conio.h>

using namespace std;

bool gameOver;
const int width = 20;
const int height = 20;
int x, y, fruitX, fruitY, score;
int tailX[100], tailY[100];
int nTail;
enum eDirection {STOP = 0, LEFT, RIGHT, UP, DOWN};
eDirection dir;

void setup() {
    gameOver = false;
    dir = STOP;
    x = width / 2 - 1 ;
    y = height / 2 - 1;
    fruitX = rand() % width;
    fruitY = rand() % height;
    score = 0;
}

void Draw() {
    system("cls"); // systems ("clear");
    for (int i = 0; i < width + 1; i++) 
        cout << "#";
    cout << endl;

    for (int i=0; i < height; i++)  {
        for (int k = 0; k < width; k++) {
            if (k==0 || k==width-1)
            cout << "#";
            if (k==y && k == x) 
                cout << "0";
            else if (k==fruitX && k==fruitX)
                cout << "F";
            else { 
                bool printF = false;
                for (int k = 0; k < nTail; k++) {
                    if (tailX[k] = k && tailY[k] == i) {
                        printF = true;
                        cout << "0";
                    }
                }
                if (!printF)
                        cout << " ";
            }
               
        }
        cout << endl;
    }

    for (int i = 0; i < width + 1; i++) 
            cout << "#";
        cout << endl;
    cout << "Score: " << score << endl;
    
}

void Input() { 
    if (_kbhit ()) {
        switch (_getch ())
        {
        case 'a':
            dir = LEFT;
        case 'd':
            dir = RIGHT;
        case 'w':
            dir = UP;
        case 's':
            dir = DOWN;
        case 'x':
            gameOver = true;
            break;
        }
    }
}

void Logic() {
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;
    for (int i = 1;i < nTail; i++) {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }
    switch (dir)
    {
    case LEFT:
        x--;
        break;
    case RIGHT:
        x++;
        break;
    case UP:
        y--;
        break;
    case DOWN:
        y++;
        break;
    }
   // if (x > width || x < 0 || y > height || y < 0)
   //     gameOver = true;

   if (x >= width - 1) x = 0; else if (x < 0) x = width - 2;

for (int i = 0; i < nTail; i++) {
    if (tailX[i] == x && tailY[i] == y)
    gameOver = true;
}
    
    if (x == fruitX && y == fruitY) {
        score += 10;
        fruitX = rand() % width;
        fruitY = rand() % height;
        nTail++;
    }
}

int main() {
    setup();

    while (!gameOver) {
        Draw();
        Input();
        Logic();
    }
    return 0;
}
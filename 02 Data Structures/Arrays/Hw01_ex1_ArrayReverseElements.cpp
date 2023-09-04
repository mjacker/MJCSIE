/** DATA Structure - 2022/04/05
 * @student:            -------------------------------
 * @topic:              Delete element in Array
 * @profesor:           ---------------
 * @teacherasistand:    ------------
 */
    /**
     * @exercise_number: 1 
     * 
     * Write a program that prompts the user to enter an array of integer (7 elements), reverses a array and prints it on the screen.
     */

#include <iostream>
using namespace std;

// Functions declarations:
void printArray(int * pointerToArray, int arrayLenght);
void reverseArray (int * arraypa, int arrayLengt);

int main(void)
{
    // variable declarations
    int array[7] = {11, 22, 33, 44, 55, 66, 77};
    int arrayLengt = sizeof(array)/sizeof(array[0]);

    // Call Print array Funtion
    printArray(array, arrayLengt);

    // Call reverse function witch you can reverse array elements
    reverseArray(array, arrayLengt);

    // Call Print array Funtion
    std::cout << endl;
    printArray(array, arrayLengt);

    return 0;
}

void printArray(int * pointerToArray, int arrayLenght){
    std::cout << "[";
    for (int i = 0; i < arrayLenght; i++){
        if (i < arrayLenght - 1){
            std::cout << *pointerToArray << ", ";
            pointerToArray++;
        }
        else{
            std::cout << *pointerToArray << "]";
            pointerToArray++;
        }
    }
}

void reverseArray (int * arraypa, int arrayLengt){
    int *initialPointer = arraypa;
    int *finalPointer = arraypa + (arrayLengt - 1);

    /* Here just verify pointer working well.
    std::cout << endl;
    std::cout << "First element: " << *initialPointer << std::endl;
    std::cout << "Last element: " << *finalPointer << std::endl;*/

    int tmp;
    while (initialPointer < finalPointer)
    {
        tmp = *initialPointer;
        *initialPointer = *finalPointer;
        *finalPointer = tmp;
        initialPointer++;
        finalPointer--;
    }
}

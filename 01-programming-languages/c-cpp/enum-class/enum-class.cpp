#include <iostream>

using namespace std;

enum Color { red, green, glue};
enum class Animal { dog, cat, bird, human};

int main (int argc, char *argv[]){

	Color my_color = green;
	cout << "enum Color: " << my_color << std::endl;

	Animal an_animal = Animal::cat;
	cout << "enum class Animal: " << static_cast<int>(an_animal) << std::endl;

	return 0;
}

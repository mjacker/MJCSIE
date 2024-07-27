#include <stdio.h>
void menuHandler();	
int calculator();
int menu(int o);
int main(int c, char** argv){

	menuHandler();

	return 0;
}

void menuHandler(){
	int option_level = 1;

	do
	{
		switch(option_level){
			case 1: option_level =  menu(1); break;
			//case 2: option_level =  menu(2); break;
			//case 3: option_level =  menu(3); break;
			default: option_level = 0; break;
		}
	}
	while (option_level > 0);
}

int menu(int o){
	printf("\n\n------------------\n");
	printf("Current menu level: %d\n", o);
	char option, null;
	
	//if option_level == 0{
	printf("a) Open calculator\n");
	printf("b) Do B\n");
	printf("c) Do C\n");
	printf("z) Exit. \n");
	printf(">> ");
	scanf("%c", &option);
	switch (option){
		case 'a': {printf("Opening the calculator...\n"); calculator();}; break;
		case 'b': printf("HACIENDO  B...\n"); break;
		case 'c': printf("HACIENDO  C...\n"); break;
		case 'z': o = o - 1; break;
		default: printf("Invalid option!\n");;
	}
	printf("Press enter to continue...");
	getchar();
	return o;
}

int calculator(){
	int number_1, number_2, result;
	int local_option = 0;

	printf("Enter first number: ");
	scanf("%d", &number_1);
	printf("Enter second number: ");
	scanf("%d", &number_2);
	printf("What operation do you want to do?\n");
	printf("1) Addition.\n");
	printf("2) Subtraction.\n");
	printf("3) Multiplicacion.\n");
	printf("4) Divition.\n");
	scanf("%d", &local_option);
	switch(local_option){
		case 1: result = number_1 + number_2; break;
		case 2: result = number_1 - number_2; break;
		case 3: result = number_1 * number_2; break;
		case 4: {
					  if (number_2 == 0) {printf("Cant divide with zero.\n"); return -1;}
					  else result = number_1 / number_2; break;
				  }
	}
	printf("The result is: %d.\n", result);
	return 0;
}

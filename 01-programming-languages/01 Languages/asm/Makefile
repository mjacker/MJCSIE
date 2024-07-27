all: out

hello.o: hello.asm
	nasm -f elf64 hello.asm

out: hello.o
	ld hello.o -o out

run: 
	make out
	./out

clean:
	rm out *.o

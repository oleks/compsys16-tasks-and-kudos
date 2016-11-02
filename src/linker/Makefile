GCC = gcc
LD = ld
FLAGS = -c -o

who_is_first: combined.o
	$(GCC) -o who_is_first combined.o
#	$(LD) -o who_is_first linker.ld *.o --dynamic-linker=/lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o /lib/crtn.o -lc -e _start

combined.o: main.o func1.o func2.o
	$(LD) -o combined.o -r -T linker.ld main.o func1.o func2.o

main.o: main.c
	$(GCC) $(FLAGS) main.o main.c

func1.o: func1.c
	$(GCC) $(FLAGS) func1.o func1.c

func2.o: func2.c
	$(GCC) $(FLAGS) func2.o func2.c

clean:
	rm *.o who_is_first

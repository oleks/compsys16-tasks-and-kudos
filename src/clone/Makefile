DOC=$(patsubst %.asciidoc,%.html,$(wildcard *.asciidoc))
SRC=$(wildcard *.c)
BIN=$(patsubst %.c,%.bin,$(SRC))

CC=gcc
CFLAGS=-Wall -Werror -Wextra -pedantic -std=c11

all: $(DOC) $(BIN)

%.html: %.asciidoc $(SRC) Makefile
	asciidoctor $*.asciidoc

%.bin: %.c Makefile
	$(CC) $(CFLAGS) -o $*.bin $*.c

clean:
	rm -f *.html

.PHONY: clean all

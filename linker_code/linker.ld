/* OUTPUT_FORMAT(elf64-x86-64) */

SECTIONS {
    .text : {
        main.o  (.text)
        __first_pointer  = .;
        func1.o (.text)
        __second_pointer = .;
        func2.o (.text)
    }

    /* .text : {
        main.o  (.text)
        __first_pointer  = .;
        func2.o (.text)
        __second_pointer = .;
        func1.o (.text)
    } */

    .data : { *(.data) } 
    .bss : { *(.bss) } 
}

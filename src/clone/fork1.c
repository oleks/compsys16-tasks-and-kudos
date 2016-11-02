#include <sys/wait.h>   // wait
#include <sys/types.h>  // pid_t
#include <stdio.h>      // printf
#include <unistd.h>     // getpid, fork
#include <error.h>      // error
#include <errno.h>      // errno

int main() {
  int datum = 1337;
  pid_t pid;

  pid = fork();
  if (pid < 0) {
    error(1, errno, "Fork failed");
  }

  if (pid == 0) {
    printf("A0: %d\n", datum);
    printf("A1: %p\n", (void*)&datum);
    datum = 42;
    printf("A2: %d\n", datum);
  } else {
    wait(NULL);
    printf("B0: %d\n", datum);
    printf("B1: %p\n", (void*)&datum);
    datum = 43;
    printf("B2: %d\n", datum);
  }

  return 0;
}

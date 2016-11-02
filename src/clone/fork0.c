#include <sys/wait.h>   // wait
#include <sys/types.h>  // pid_t
#include <stdio.h>      // printf
#include <unistd.h>     // getpid, fork
#include <error.h>      // error
#include <errno.h>      // errno

int main() {
  pid_t pid0, pid1, pid2;

  pid0 = getpid();

  pid1 = fork();
  if (pid1 < 0) {
    error(1, errno, "Fork failed");
  }

  pid2 = getpid();

  if (pid1 == 0) {
    printf("A0: %d\n", pid0);
    printf("A1: %d\n", pid1);
    printf("A2: %d\n", pid2);
  } else {
    wait(NULL);
    printf("B0: %d\n", pid0);
    printf("B1: %d\n", pid1);
    printf("B2: %d\n", pid2);
  }

  return 0;
}

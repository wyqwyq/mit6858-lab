#include<stdio.h>

int main(int argc, char **argv)
{
  char buff[5];
  if(argc != 2) {
  puts("Need an argument!");
  _exit(1);
  }
  printf("Exploiting via returnig into libc function\n");
  strcpy(buff, argv[1]); 
  printf("\nYou typed [%s]\n\n", buff);
  return(0);
}

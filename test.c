/* whoami.c - a simple implementation of whoami utility */
#include <pwd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int C(){
  return 3;
}

int B(){
  return C();
}


int A(){
  return B();
}

int who_am_i (void)
{
  struct passwd *pw;
  char *user = NULL;

  pw = getpwuid (geteuid ());
  if (pw)
    user = pw->pw_name;
  else if ((user = getenv ("USER")) == NULL)
    {
      fprintf (stderr, "I don't know!\n");
      return 1;
    }
  printf ("%s\n", user);
  return 0;
}

int main (int argc, char **argv)
{
  int a = A();
  if (argc > 1)
    {
      fprintf (stderr, "usage: whoami\n");
      return 1;
    }
  return who_am_i ();
}
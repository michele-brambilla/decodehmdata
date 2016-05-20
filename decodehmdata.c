/**
* This is a little program which reads the content of a historgram
* memory data file and prints the values to stdout
* 
* Mark Koennecke, Gerd Theidel, September 2005
* Michele Brambilla, April 2016
*/
#include <stdio.h>

int main(int argc, char *argv[]){
  FILE *fd = NULL;
  int val,index=0;
	
  if(argc < 2){
    puts("Usage:\n\tdecodehmdata datafile\n");
    exit(1);
  }
	
  fd = fopen(argv[1],"r");
  if(fd == NULL){
    puts("Cannot open data file\n");
    exit(1);
  }
  while(fread(&val,sizeof(int),1,fd) == 1){
    fprintf(stdout,"%d\t%d\n",index,val);
    ++index;
  }
  fclose(fd);
  exit(0);
}


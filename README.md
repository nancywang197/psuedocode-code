# psuedocode-code
Dataset Source: SpOC Dataset from https://arxiv.org/abs/1906.04908 paper 
- TSV file
- Each line contains a line of psuedocode, its corresponding code, the line number, and the indent level

Writing to JSON:
1. make list to store pairs of psuedocode and corresponding code
2. read line
3. delimit to tabs to get psuedocode line, code line, line number, indent level
4. add indentation to psuedocode and code line
5. add lines of psuedocode and code belonging to the same block/prompt together using the line number as a guide
6. if line # = 0, then the block of code and psuedocode is done
7. add the pairs of psudeocode and code to list
8. when done parsing the file, write the list to json 

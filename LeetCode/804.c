int uniqueMorseRepresentations(char** words, int wordsSize) {
    if(wordsSize == 0) return 0;
    char* morse[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    char translated[wordsSize][144];
    
    for(int i=0; i<wordsSize; i++) {
        translated[i][0] = '\0';
        for(int j=0; j<strlen(words[i]); j++) {
            int wordIndex = words[i][j] - 'a';
            strcat(translated[i], morse[wordIndex]);
        }
    }
    
    for(int i=0; i<wordsSize; i++) {
        for(int j=0; j<wordsSize; j++) {
            if(i==j) continue;
            if(!strcmp(translated[i], translated[j])) {
                translated[j][0] = '\0';
            }
        }
    }
    
    int total = 0;
    for(int i=0; i<wordsSize; i++) {
        if(strlen(translated[i])) {
            total++;
        }
    }
    
    return total;
}
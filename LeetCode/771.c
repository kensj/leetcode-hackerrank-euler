int numJewelsInStones(char* J, char* S) {
    int j_len = strlen(J);
    int s_len = strlen(S);
    int total = 0;
    for(int j=0; j<j_len; j++) {
        for(int s=0; s<s_len; s++) {
            if(J[j] == S[s]) total++;
        }
    }
    return total;
}
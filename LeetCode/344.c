char* reverseString(char* s) {
    if(!s) return s;
    int right = strlen(s) - 1;
    int left = 0;
    while(right > left) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        right--;
        left++;
    }
    return s;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    char** list = malloc(sizeof(char*) * n);
    for(int i=0; i<n; i++) {
        list[i] = malloc(sizeof(char) * 10);
        list[i][0] = '\0';
        if(!((i+1)%15)) strcpy(list[i], "FizzBuzz");
        else if(!((i+1)%5)) strcpy(list[i], "Buzz");
        else if(!((i+1)%3)) strcpy(list[i], "Fizz");
        else sprintf(list[i], "%d", i+1);
    }
    *returnSize = n;
    return list;
}
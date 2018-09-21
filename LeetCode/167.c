/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* ret = malloc(sizeof(int) * 2);
    for(int i=0; i<numbersSize;i++) {
        for(int j=i+1;j<numbersSize;j++) {
            int total = numbers[i] + numbers[j];
            if(total == target) {
                ret[0] = i+1;
                ret[1] = j+1;
                *returnSize = 2;
                break;
            }
        }
    }
    return ret;
}
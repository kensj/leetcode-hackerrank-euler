/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int* ret = malloc(sizeof(int)*2);
    for(int i=0; i<numsSize; i++) {
        for(int j=0; j<numsSize; j++) {
            int total = nums[i] + nums[j];
            if(i != j && total == target) {
                *ret = i;
                ret[1] = j;
            }
        }
    }
    return ret;
}

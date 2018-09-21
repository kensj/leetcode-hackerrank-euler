void moveZeroes(int* nums, int numsSize) {
    for(int i=0; i<numsSize-1; i++) {
        if(!nums[i]) {
            int j=i+1;
            while(j<numsSize && !nums[j]) j++;
            if(j<numsSize) {
                nums[i] = nums[j];
                nums[j] = 0;
            }
        }
    }
}

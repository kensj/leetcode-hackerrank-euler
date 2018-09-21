int simpleArraySum(int n, int ar_size, int* ar) {
    // Complete this function
    int total = 0;
    for(int i=0;i<ar_size;i++) {
        total += ar[i];
    }
    return total;
}

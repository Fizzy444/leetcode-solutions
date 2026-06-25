int removeDuplicates(int* nums, int numsSize) {
    int k=0,j;
    for (j=0;j<numsSize;j++){
        if (nums[j]!=nums[k]){
            k++;
            nums[k]=nums[j];
        }
    }
    return k+1;
}
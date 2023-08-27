int removeDuplicates(int *nums, int numsSize) {
  int previous = !nums[0];
  int read_location = 0;
  int write_location = 0;
  int k = 0;
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == previous) {
      read_location++;
      continue;
    }
    previous = nums[read_location];
    nums[write_location] = previous;
    read_location++;
    write_location++;
    k++;
  }
  return k;
}
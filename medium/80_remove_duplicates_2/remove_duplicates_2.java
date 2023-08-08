class Solution {
    public int removeDuplicates(int[] nums) {
        int read_location = 0;
        int write_location = 0;
        int k = 0;
        int previous = nums[0] + 1;
        int previous_count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[read_location] == previous) {
                previous_count++;
            } else {
                previous_count = 0;
            }
            if (previous_count >= 2) {
                read_location++;
                continue;
            }
            previous = nums[read_location];
            nums[write_location] = previous;
            write_location++;
            read_location++;
            k++;
        }
        return k;
    }
}
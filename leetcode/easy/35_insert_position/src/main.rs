fn main() {
    println!("{}", Solution::search_insert(vec![1, 3, 5, 6], 5));
}

struct Solution();

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        if target < nums[0] {
            return 0;
        }
        Solution::search(&nums, 0, nums.len(), target)
    }

    pub fn search(nums: &[i32], start: usize, end: usize, target: i32) -> i32 {
        let middle = start + (end - start) / 2;
        if nums[middle] == target {
            return middle as i32;
        }
        if end - start == 1 {
            return end as i32;
        }
        if target < nums[middle] {
            Solution::search(nums, start, middle, target)
        } else {
            Solution::search(nums, middle, end, target)
        }
    }
}

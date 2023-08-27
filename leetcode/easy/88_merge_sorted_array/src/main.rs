impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut pos1 = 0;
        let mut pos2 = 0;
        let mut result = vec![];
        for _ in 0..(m + n) {
            if pos1 == m as usize {
                result.push(nums2[pos2]);
                pos2 += 1;
                continue;
            }
            if pos2 == n as usize {
                result.push(nums1[pos1]);
                pos1 += 1;
                continue;
            }
            if nums2[pos2] < nums1[pos1] {
                result.push(nums2[pos2]);
                pos2 += 1;
            } else {
                result.push(nums1[pos1]);
                pos1 += 1;
            }
        }
        nums1[..((n + m) as usize)].copy_from_slice(&result[..((n + m) as usize)]);
    }
}

struct Solution {}

pub fn main() {}

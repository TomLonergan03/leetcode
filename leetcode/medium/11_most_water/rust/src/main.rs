fn main() {
    println!("{}", Solution::max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]));
    println!("{}", Solution::max_area(vec![1, 2, 4, 3]));
}

struct Solution();

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_volume = 0;
        for _ in 0..height.len() - 1 {
            let width = (right - left) as i32;
            let volume_height = height[left].min(height[right]);
            let volume = width * volume_height;
            max_volume = max_volume.max(volume);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        max_volume
    }
}

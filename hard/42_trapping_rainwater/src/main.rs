fn main() {
    println!("{}", Solution::trap(vec![4, 2, 0, 3, 2, 5]));
}

struct Solution();

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let x_size = height.len();
        let y_size = height.iter().max().unwrap().to_owned() as usize;

        let mut count = 0;

        for y in 0..=y_size {
            let mut left_wall = usize::MAX;
            for x in 0..x_size {
                if height[x] as usize >= y {
                    if left_wall < x {
                        count += x - left_wall - 1;
                    }
                    left_wall = x;
                }
            }
        }
        count as i32
    }
}

fn main() {
    println!("{}", Solution::length_of_last_word("abc def".to_string()));
}

struct Solution();

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut chars_since_space = 0;
        for char in s.trim().chars() {
            if char == ' ' {
                chars_since_space = 0;
                continue;
            }
            chars_since_space += 1;
        }
        chars_since_space
    }
}

use std::collections::HashMap;

fn main() {
    println!(
        "{:?}",
        Solution::is_isomorphic("egg".to_string(), "add".to_string())
    );
    println!(
        "{:?}",
        Solution::is_isomorphic("foo".to_string(), "bar".to_string())
    );
    println!(
        "{:?}",
        Solution::is_isomorphic("paper".to_string(), "title".to_string())
    );
}

struct Solution();

impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut s_letter_to_int: HashMap<char, u32> = HashMap::new();
        let s: Vec<char> = s.chars().collect();
        let mut s_int: Vec<u32> = vec![];
        let mut s_max = 0;
        (0..s.len()).for_each(|i| match s_letter_to_int.get(&s[i]) {
            Some(number) => s_int.push(*number),
            None => {
                s_letter_to_int.insert(s[i], s_max);
                s_int.push(s_max);
                s_max += 1;
            }
        });
        let mut t_letter_to_int: HashMap<char, u32> = HashMap::new();
        let t: Vec<char> = t.chars().collect();
        let mut t_int: Vec<u32> = vec![];
        let mut t_max = 0;
        (0..t.len()).for_each(|i| match t_letter_to_int.get(&t[i]) {
            Some(number) => t_int.push(*number),
            None => {
                t_letter_to_int.insert(t[i], t_max);
                t_int.push(t_max);
                t_max += 1;
            }
        });
        for i in 0..s.len() {
            if s_int[i] != t_int[i] {
                return false;
            }
        }
        true
    }
}

fn main() {
    println!(
        "{}",
        Solution::can_complete_circuit(vec![1, 2, 3, 4, 5], vec![3, 4, 5, 1, 2])
    );
}

struct Solution();

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        let mut total_gas = 0;
        let mut total_cost = 0;
        let mut current_gas = 0;
        let mut starting_point = 0;
        for i in 0..n {
            total_gas += gas[i];
            total_cost += cost[i];
            current_gas += gas[i] - cost[i];
            if current_gas < 0 {
                starting_point = i + 1;
                current_gas = 0
            }
        }
        if total_gas < total_cost {
            -1
        } else {
            starting_point as i32
        }
    }
}

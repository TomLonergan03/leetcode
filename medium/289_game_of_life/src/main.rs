fn main() {
    let mut board = vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];
    Solution::game_of_life(&mut board);
    println!("{:?}", board);
    assert_eq!(
        board,
        vec![vec![0, 0, 0], vec![1, 0, 1], vec![0, 1, 1], vec![0, 1, 0]]
    );
    let mut board = vec![vec![1, 1], vec![1, 0]];
    Solution::game_of_life(&mut board);
    assert_eq!(board, vec![vec![1, 1], vec![1, 1]]);
}

struct Solution();

impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        let mut new_board = board.clone();
        (0..board.len()).for_each(|x| {
            (0..board[0].len()).for_each(|y| {
                let cell = board[x][y];
                let neighbours = Solution::count_neighbours(board, x, y);
                if cell == 1 {
                    if (2..=3).contains(&neighbours) {
                        new_board[x][y] = 1;
                    } else {
                        new_board[x][y] = 0;
                    }
                } else if neighbours == 3 {
                    new_board[x][y] = 1;
                }
            });
        });
        (0..board.len()).for_each(|x| {
            (0..board[0].len()).for_each(|y| board[x][y] = new_board[x][y]);
        });
    }

    pub fn count_neighbours(board: &Vec<Vec<i32>>, x: usize, y: usize) -> i32 {
        let mut count = 0;
        let left = 0.max(x as i32 - 1) as usize;
        let right = (x + 1).min(board.len() - 1);
        let bottom = 0.max(y as i32 - 1) as usize;
        let top = (y + 1).min(board[0].len() - 1);
        (left..=right).for_each(|x| {
            (bottom..=top).for_each(|y| count += board[x][y]);
        });
        count -= board[x][y];
        count
    }
}

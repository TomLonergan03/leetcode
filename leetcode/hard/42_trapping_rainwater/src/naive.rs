fn main() {
    println!("{}", Solution::trap(vec![4, 2, 0, 3, 2, 5]));
}

struct Solution();

#[derive(Clone, Copy, PartialEq)]
enum Cell {
    Air,
    Wall,
    Water,
}

struct Map {
    // outer vec is y coord
    // inner vec is x coord
    map: Vec<Vec<Cell>>,
    x_size: usize,
    y_size: usize,
}

impl Map {
    pub fn new(heightmap: Vec<i32>) -> Map {
        let x_size = heightmap.len();
        let y_size = heightmap.iter().max().unwrap().to_owned() as usize;
        let mut map = Map {
            map: vec![vec![Cell::Air; x_size]; y_size],
            x_size,
            y_size,
        };
        // map.print();

        (0..x_size).for_each(|x| {
            for y in 0..heightmap[x] as usize {
                map.set_cell(x, y, Cell::Wall);
            }
        });
        map
    }

    /// Return true if there is a wall at (x, y)
    fn get_cell(&self, x: usize, y: usize) -> Cell {
        self.map[y][x]
    }

    fn set_cell(&mut self, x: usize, y: usize, contents: Cell) {
        self.map[y][x] = contents;
    }

    pub fn count_pools(mut self) -> i32 {
        let mut count = 0;
        for y in 0..self.y_size {
            let mut left_wall = usize::MAX;
            for x in 0..self.x_size {
                if self.get_cell(x, y) == Cell::Wall {
                    if left_wall < x {
                        count += x - left_wall - 1;
                        // for water_x in left_wall + 1..x {
                        //     self.set_cell(pretty_x, y, Cell::Water)
                        // }
                    }
                    left_wall = x;
                }
            }
        }
        // self.print();
        count as i32
    }

    pub fn print(&self) {
        for y in (0..self.y_size).rev() {
            for x in 0..self.x_size {
                match self.get_cell(x, y) {
                    Cell::Wall => print!("1"),
                    Cell::Air => print!("0"),
                    Cell::Water => print!("W"),
                }
            }
            println!();
        }
        println!();
    }
}

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let map = Map::new(height);
        // map.print();
        map.count_pools()
    }
}

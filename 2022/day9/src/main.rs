use std::fs;
use std::collections::HashMap;

fn main() {
    let input = fs::read_to_string(r"input.txt").expect("REASON");
    let input: Vec<(char, i32)> = input
        .lines()console
        .map(|line| {
            let mut split = line.split_whitespace();
            let c = split.next().unwrap().chars().next().unwrap();
            let i = split.next().unwrap().parse::<i32>().unwrap();
            (c, i)
        })
        .collect();

    let mut grid = InfiniteGrid::new();
    for (c, i) in input {
        grid.move_h(c, i);
        grid.print_grid();
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        print!("{}[2J", 27 as char);
    }
    let mut count = 0;
    for (_, (_, c2)) in grid.grid.iter() {
        if *c2 == 'T' {
            count += 1;
        }
    }
    
    println!("Count: {}", count);
    println!("Moves H: {}, Moves T: {}", grid.moves_h, grid.moves_t);
}

#[derive(Debug)]
struct InfiniteGrid {
    grid: HashMap<(i32, i32), (char, char)>,
    current_h: (i32, i32),
    current_t: (i32, i32),
    moves_h: i32,
    moves_t: i32,
}

impl InfiniteGrid {
    fn new() -> Self {
        let mut grid = HashMap::new();
        grid.insert((0, 0), ('H', 'T'));
        let current_h = (0, 0);
        let current_t = (0, 0);
        let moves_h = 0;
        let moves_t = 0;
        InfiniteGrid {
            grid,
            current_h,
            current_t,
            moves_h,
            moves_t,
        }
    }

    fn get(&self, x: i32, y: i32) -> (char, char) {
        match self.grid.get(&(x, y)) {
            Some(c) => *c,
            None => ('.', '.'),
        }
    }

    fn set(&mut self, x: i32, y: i32, c1: char, c2: char) {
        self.grid.insert((x, y), (c1, c2));
    }

    fn is_touching(&self) -> bool {
        let (xh, yh) = self.current_h;
        let (xt, yt) = self.current_t;
        if xh == xt && yh == yt {
            return true;
        }
        if xh == xt && (yh - 1 == yt || yh + 1 == yt) {
            return true;
        }
        if yh == yt && (xh - 1 == xt || xh + 1 == xt) {
            return true;
        }
        if (xh - 1 == xt || xh + 1 == xt) && (yh - 1 == yt || yh + 1 == yt) {
            return true;
        }
        false
    }

    fn move_h(&mut self, direction: char, steps: i32) {
        match direction {
            'U' => {
                for _ in 1..=steps {
                    let (x, y) = self.current_h;
                    self.moves_h += 1;
                    // self.set(x, y, '.', self.get(x, y).1);
                    self.set(x, y + 1, 'H', self.get(x, y + 1).1);
                    self.current_h = (x, y + 1);
                    if !self.is_touching() {
                        let (xt, yt) = self.closest();
                        self.move_t(xt, yt);
                    }
                }
            }
            'D' => {
                for _ in 1..=steps {
                    let (x, y) = self.current_h;
                    self.moves_h += 1;
                    // self.set(x, y, '.', self.get(x, y).1);
                    self.set(x, y - 1, 'H', self.get(x, y - 1).1);
                    self.current_h = (x, y - 1);
                    if !self.is_touching() {
                        let (xt, yt) = self.closest();
                        self.move_t(xt, yt);
                    }
                }
            }
            'R' => {
                for _ in 1..=steps {
                    let (x, y) = self.current_h;
                    self.moves_h += 1;
                    // self.set(x, y, '.', self.get(x, y).1);
                    self.set(x + 1, y, 'H', self.get(x + 1, y).1);
                    self.current_h = (x + 1, y);
                    if !self.is_touching() {
                        let (xt, yt) = self.closest();
                        self.move_t(xt, yt);
                    }
                }
            }
            'L' => {
                for _ in 1..=steps {
                    let (x, y) = self.current_h;
                    self.moves_h += 1;
                    // self.set(x, y, '.', self.get(x, y).1);
                    self.set(x - 1, y, 'H', self.get(x - 1, y).1);
                    self.current_h = (x - 1, y);
                    if !self.is_touching() {
                        let (xt, yt) = self.closest();
                        self.move_t(xt, yt);
                    }
                }
            }
            _ => panic!("Invalid direction"),
        }
    }

    fn move_t(&mut self, xt: i32, yt: i32) {
        let (x, y) = self.current_t;
        self.moves_t += 1;
        if x == xt && y == yt {
            return;
        } else {
            // self.set(x, y, self.get(x, y).0, '.');
            self.set(xt, yt, self.get(xt, yt).0, 'T');
            self.current_t = (xt, yt);
        }
    }

    fn touching_points(&self) -> Vec<(i32, i32)> {
        let mut points = Vec::new();
        let (xh, yh) = self.current_h;
        points.push((xh, yh));
        points.push((xh - 1, yh));
        points.push((xh + 1, yh));
        points.push((xh, yh - 1));
        points.push((xh, yh + 1));
        points
    }

    fn closest(&self) -> (i32, i32) {
        let (xt, yt) = self.current_t;
        let mut min_dist = 1000000.0;
        let mut min_point = (0, 0);
        for (x, y) in self.touching_points() {
            let dist = (((x - xt).abs().pow(2) + (y - yt).abs().pow(2)) as f32).sqrt();
            if dist < min_dist {
                min_dist = dist;
                min_point = (x, y);
            }
        }
        min_point
    }

    fn print_scope(&self) {
        let (xh, yh) = self.current_h;
        let (xt, yt) = self.current_t;
        let mut min_x = xh;
        let mut max_x = xh;
        let mut min_y = yh;
        let mut max_y = yh;
        if xt < min_x {
            min_x = xt;
        }
        if xt > max_x {
            max_x = xt;
        }
        if yt < min_y {
            min_y = yt;
        }
        if yt > max_y {
            max_y = yt;
        }
        for y in (min_y - 5)..=(max_y + 5) {
            print!("{:3} ", y);
            for x in (min_x - 5)..=(max_x + 5) {
                if (x == xh && y == yh ) && (x == xt && y == yt) {
                    print!(" X  ");
                } else if x == xh && y == yh {
                    print!(" H  ");
                } else if x == xt && y == yt {
                    print!(" T  ");
                } else {
                    print!(" .  ");
                }
            }
            println!();
        }
        print!("    ");
        for x in (min_x - 5)..=(max_x + 5) {
            if x < 10 && x > -1 {
                print!("{}   ", x);
            } else if x < 100 && x > 10{
                print!("{}  ", x);
            } else if x < 1000 && x > -100{
                print!("{} ", x);
            } else {
                print!("{}", x);
            }
        }
        println!();
    }

    fn print_grid(&self) {
        min_y = 0;
        max_y = 0;
        min_x = 0;
        max_x = 0;
        for (x, y) in self.grid.keys() {
            if *x < min_x {
                min_x = *x;
            }
            if *x > max_x {
                max_x = *x;
            }
            if *y < min_y {
                min_y = *y;
            }
            if *y > max_y {
                max_y = *y;
            }
        }
        for y in min_y..=max_y {
            for x in min_x..=max_x {
                if (x == xh && y == yh ) && (x == xt && y == yt) {
                    print!(" X  ");
                } else if x == xh && y == yh {
                    print!(" H  ");
                } else if x == xt && y == yt {
                    print!(" T  ");
                } else {
                    print!(" .  ");
                }
            }
            println!();
        }
    }
}



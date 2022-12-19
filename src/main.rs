use std::io;

fn main() {
    let n = read_ln();
    let h = read_ln();
    let w = read_ln();

    let ans = (n - h + 1) * (n - w + 1);
    println!("{}", ans);
}

fn read_ln() -> i32 {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: i32 = n.trim().parse().expect("Please type a number!");
    n
}

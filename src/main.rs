use std::io;

fn main() {
    let n = read_ln();
    let h = read_ln();
    let w = read_ln();

    let ans = (n - h + 1) * (n - w + 1);
    println!("{}", ans);
}

fn read_ln() -> i32 {
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .expect("Failed to read line");
    buf.trim().parse().expect("Please type a number!")
}

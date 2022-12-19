use std::io;

const ASCII_UPPERCASE: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn main() {
    let k = read_ln();

    let ans = &ASCII_UPPERCASE[..k];
    println!("{}", ans);
}

fn read_ln() -> usize {
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .expect("Failed to read line");
    buf.trim().parse().expect("Please type a number!")
}

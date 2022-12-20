use proconio::input;
use std::cmp;
// use std::io;

// const ASCII_UPPERCASE: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn main() {
    // input
    // let k = read_ln();
    input! {
        (a, b, c, d): (i64, i64, i64, i64),
    }

    // main
    // let ans = &ASCII_UPPERCASE[..k];
    let ans = cmp::max(a, c) <= cmp::min(b, d);

    // output
    println!("{}", if ans { "Yes" } else { "No" });
}

// fn read_ln() -> usize {
//     let mut buf = String::new();
//     io::stdin()
//         .read_line(&mut buf)
//         .expect("Failed to read line");
//     buf.trim().parse().expect("Please type a number!")
// }

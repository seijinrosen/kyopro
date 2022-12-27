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
    // let mut vec: Vec<i32> = Vec::new();
    // for i in 1..=a {
    //     vec.push(i);
    // }
    // vec.push(-vec.iter().sum::<i32>());
    // let ans = match day.as_str() {
    //     "Monday" => 5,
    //     "Tuesday" => 4,
    //     _ => 0,
    // };

    // output
    println!("{}", ans);
    println!("{}", if ans { "Yes" } else { "No" });
    // println!("{}", itertools::join(vec, " "));
}

// fn read_ln() -> usize {
//     let mut buf = String::new();
//     io::stdin()
//         .read_line(&mut buf)
//         .expect("Failed to read line");
//     buf.trim().parse().expect("Please type a number!")
// }

// fn is_leap(y: i32) -> bool {
//     match y {
//         y if y % 400 == 0 => true,
//         y if y % 100 == 0 => false,
//         _ => y % 4 == 0,
//     }
// }

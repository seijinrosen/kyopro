use proconio::input;
use std::cmp;

// const ASCII_UPPERCASE: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn main() {
    input! {
        (a, b, c, d): (i64, i64, i64, i64),
    }

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

    println!("{}", ans);
    println!("{}", if ans { "Yes" } else { "No" });
    // println!("{}", itertools::join(vec, " "));
}

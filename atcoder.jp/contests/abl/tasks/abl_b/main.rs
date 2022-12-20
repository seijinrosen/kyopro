use proconio::input;
use std::cmp;

fn main() {
    input! {
        (a, b, c, d): (i64, i64, i64, i64),
    }

    let ans = cmp::max(a, c) <= cmp::min(b, d);
    println!("{}", if ans { "Yes" } else { "No" });
}

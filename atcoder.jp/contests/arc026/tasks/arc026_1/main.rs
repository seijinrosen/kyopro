use proconio::input;
use std::cmp;

fn main() {
    input! {
        (n, a, b): (i32, i32, i32),
    }

    let bb = cmp::min(5, n);
    let aa = n - bb;
    let ans = a * aa + b * bb;

    println!("{}", ans);
}

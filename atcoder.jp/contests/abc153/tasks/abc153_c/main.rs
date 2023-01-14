use itertools::{sorted, Itertools};
use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        h: [i64; n],
    }

    let ans: i64 = sorted(h).rev().dropping(k).sum();

    println!("{}", ans);
}

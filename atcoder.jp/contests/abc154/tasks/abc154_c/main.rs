use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        a: [i32; n],
    }

    let hs: HashSet<i32> = a.into_iter().collect();
    let ans = hs.len() == n;

    println!("{}", if ans { "YES" } else { "NO" });
}

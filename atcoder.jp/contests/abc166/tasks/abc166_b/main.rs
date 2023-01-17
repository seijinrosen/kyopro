use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [[usize]; k],
    }

    let mut hs = HashSet::new();
    for a in a {
        for a in a {
            hs.insert(a);
        }
    }

    let ans = n - hs.len();

    println!("{}", ans);
}

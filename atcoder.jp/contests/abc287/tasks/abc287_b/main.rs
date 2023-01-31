use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
        t: [String; m],
    }

    let hs: HashSet<_> = t.into_iter().collect();
    let ans = s.into_iter().filter(|s| hs.contains(&s[3..])).count();

    println!("{}", ans);
}

use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: i32,
        s: [String; n],
    }

    let hs: HashSet<String> = s.into_iter().collect();
    let ans = hs.len();

    println!("{}", ans);
}

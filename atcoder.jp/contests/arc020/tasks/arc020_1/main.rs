use std::cmp::Ordering;

use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
    }

    let ans = match a.abs().cmp(&b.abs()) {
        Ordering::Less => "Ant",
        Ordering::Equal => "Draw",
        Ordering::Greater => "Bug",
    };

    println!("{}", ans);
}

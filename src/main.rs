// use std::cmp;
// use std::collections::HashSet;

use proconio::input;
// use proconio::marker::Chars;

// use kyopro::MyString;

fn main() {
    input! {
        n: usize,
        // s: Chars,
        // a: [i32; n],
        // (x, y): (i64, i64),
        // mut s: [String; n],
    }

    let ans = n;
    // let ans = &ASCII_UPPERCASE[..k];
    // let ans = cmp::max(a, c) <= cmp::min(b, d);

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

    // let ans = is_palindrome(n.trim_end_matches('0'));
    // let ans = n.trim_end_matches('0').is_palindrome();
    // let hs: HashSet<i32> = a.into_iter().collect();

    println!("{}", ans);
    // println!("{}", if ans { "Yes" } else { "No" });
    // println!("{}", itertools::join(vec, " "));
}

// fn is_weak2(xs: &[u32]) -> bool {
//     if xs.len() < 2 {
//         return true;
//     }
//     let x = xs[0];
//     let y = xs[1];
//     let xs = &xs[1..];
//     (x + 1) % 10 == y && is_weak2(xs)
// }

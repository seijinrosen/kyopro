use std::process;

use proconio::input;

fn main() {
    input! {
        a: usize,
        mut b: usize,
        mut c: usize,
        k: usize,
    }

    for _ in 0..=k {
        if a < b && b < c {
            println!("Yes");
            process::exit(0);
        }

        if a >= b {
            b *= 2;
        } else if b >= c {
            c *= 2;
        }
    }

    println!("No");
}

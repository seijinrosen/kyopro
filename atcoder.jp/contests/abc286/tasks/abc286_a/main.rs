use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        p: usize,
        q: usize,
        r: usize,
        s: usize,
        a: [usize; n],
    }

    let ans = a[..p - 1]
        .iter()
        .chain(&a[r - 1..s])
        .chain(&a[q..r - 1])
        .chain(&a[p - 1..q])
        .chain(&a[s..])
        .join(" ");

    println!("{}", ans);
}

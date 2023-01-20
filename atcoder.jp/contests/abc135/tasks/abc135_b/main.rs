use proconio::input;

fn main() {
    input! {
        n: usize,
        p: [usize; n]
    }

    let cnt = p
        .into_iter()
        .enumerate()
        .filter(|(i, p)| i + 1 != *p)
        .count();

    let ans = cnt == 0 || cnt == 2;

    println!("{}", if ans { "YES" } else { "NO" });
}

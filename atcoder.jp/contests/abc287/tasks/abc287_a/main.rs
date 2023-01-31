use proconio::input;

fn main() {
    input! {
        n: usize,
        s: [String; n],
    }

    let mut cnt = 0;
    for s in s {
        if s == "For" {
            cnt += 1;
        }
    }

    let ans = n / 2 < cnt;

    println!("{}", if ans { "Yes" } else { "No" });
}

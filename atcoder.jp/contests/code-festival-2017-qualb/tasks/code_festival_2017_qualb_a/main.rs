use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = &s[..s.len() - 8];

    println!("{}", ans);
}

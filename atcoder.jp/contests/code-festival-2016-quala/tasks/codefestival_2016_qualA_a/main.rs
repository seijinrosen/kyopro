use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = "".to_string() + &s[..4] + " " + &s[4..];

    println!("{}", ans);
}

use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = String::from(&s[..s.len() - 1]) + "5";

    println!("{}", ans);
}

use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = s.contains("AC");

    println!("{}", if ans { "Yes" } else { "No" });
}

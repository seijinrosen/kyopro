use proconio::input;

fn main() {
    input! {
        n: String,
    }

    let ans = is_palindrome(n.trim_end_matches('0'));

    println!("{}", if ans { "Yes" } else { "No" });
}

pub fn is_palindrome(s: &str) -> bool {
    reverse(&s) == s
}

pub fn reverse(s: &str) -> String {
    s.chars().rev().collect()
}

use proconio::input;

fn main() {
    input! {
        n: String,
    }

    let ans = n.trim_end_matches('0').is_palindrome();

    println!("{}", if ans { "Yes" } else { "No" });
}

pub trait MyString {
    fn is_palindrome(&self) -> bool;
    fn reverse(&self) -> String;
}

impl MyString for str {
    fn is_palindrome(&self) -> bool {
        self.reverse() == self
    }
    fn reverse(&self) -> String {
        self.chars().rev().collect()
    }
}

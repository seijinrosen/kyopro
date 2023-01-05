use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        xs: String,
    }

    let xs = xs.to_digits();
    let is_weak = is_weak1(&xs) || is_weak2(&xs);

    println!("{}", if is_weak { "Weak" } else { "Strong" });
}

fn is_weak1(xs: &Vec<u32>) -> bool {
    let hs: HashSet<_> = xs.into_iter().collect();
    hs.len() == 1
}

fn is_weak2(xs: &[u32]) -> bool {
    if xs.len() < 2 {
        return true;
    }
    let x = xs[0];
    let y = xs[1];
    let xs = &xs[1..];
    (x + 1) % 10 == y && is_weak2(xs)
}

pub trait MyString {
    fn to_digits(&self) -> Vec<u32>;
}
impl MyString for str {
    fn to_digits(&self) -> Vec<u32> {
        self.chars().map(|c| c.to_digit(10).unwrap()).collect()
    }
}

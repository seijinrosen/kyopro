use proconio::input;
use std::cmp::Ordering;

fn main() {
    input! {
        (a, b, c): (i32, i32, i32),
    }

    let ans = solve(a, b, c).to_char();

    println!("{}", ans);
}

fn solve(a: i32, b: i32, c: i32) -> Ordering {
    match c {
        c if c.is_even() => a.abs().cmp(&b.abs()),
        _ => a.cmp(&b),
    }
}

pub trait ToChar {
    fn to_char(&self) -> char;
}
impl ToChar for Ordering {
    fn to_char(&self) -> char {
        match self {
            Ordering::Less => '<',
            Ordering::Equal => '=',
            Ordering::Greater => '>',
        }
    }
}

pub trait MyInt {
    fn is_even(&self) -> bool;
}
impl MyInt for i32 {
    fn is_even(&self) -> bool {
        self % 2 == 0
    }
}

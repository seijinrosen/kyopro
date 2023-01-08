mod int;
pub mod string;

pub use crate::int::MyInt;
pub use crate::string::MyString;

use std::cmp::Ordering;
use std::io;

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

/// うるう年かどうかを判定する。
///
/// # Examples
///
/// ```
/// use kyopro::is_leap;
///
/// assert_eq!(is_leap(1001), false);
/// assert_eq!(is_leap(2000), true);
/// assert_eq!(is_leap(2012), true);
/// assert_eq!(is_leap(2100), false);
/// ```
pub fn is_leap(year: i32) -> bool {
    match year {
        y if y % 400 == 0 => true,
        y if y % 100 == 0 => false,
        _ => year % 4 == 0,
    }
}

/// 一行読み込んで、数値に変換する。
pub fn read_ln() -> usize {
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .expect("Failed to read line");
    buf.trim().parse().expect("Please type a number!")
}

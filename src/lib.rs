use std::io;

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

/// 回文かどうかを判定する。
///
/// # Examples
///
/// ```
/// use kyopro::is_palindrome;
///
/// assert_eq!(is_palindrome("abc"), false);
/// assert_eq!(is_palindrome("abcba"), true);
/// ```
pub fn is_palindrome(s: &str) -> bool {
    reverse(&s) == s
}

/// 文字列を反転させる。
///
/// # Examples
///
/// ```
/// use kyopro::reverse;
///
/// assert_eq!(reverse("abc"), "cba");
/// ```
pub fn reverse(s: &str) -> String {
    s.chars().rev().collect()
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

/// 一行読み込んで、数値に変換する。
pub fn read_ln() -> usize {
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .expect("Failed to read line");
    buf.trim().parse().expect("Please type a number!")
}

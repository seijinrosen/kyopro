use std::{iter::Enumerate, str::Chars};

pub trait MyString {
    fn dedup(&self) -> String;
    fn enumerate(&self) -> Enumerate<Chars>;
    fn is_palindrome(&self) -> bool;
    fn reverse(&self) -> String;
    fn to_digits(&self) -> Vec<u32>;
}

impl MyString for str {
    /// 連続する文字を削除する。
    ///
    /// # Examples
    ///
    /// ```
    /// use kyopro::MyString;
    ///
    /// assert_eq!("aabbbbaaca".dedup(), "abaca");
    /// assert_eq!("aaaaa".dedup(), "a");
    /// assert_eq!("xxzaffeeeeddfkkkkllq".dedup(), "xzafedfklq");
    /// ```
    fn dedup(&self) -> String {
        let mut vec = self.as_bytes().to_vec();
        vec.dedup();
        String::from_utf8(vec).unwrap()
    }

    /// `str.chars().enumerate()` のショートハンド。
    fn enumerate(&self) -> Enumerate<Chars> {
        self.chars().enumerate()
    }

    /// 回文かどうかを判定する。
    ///
    /// # Examples
    ///
    /// ```
    /// use kyopro::MyString;
    ///
    /// assert_eq!("abc".is_palindrome(), false);
    /// assert_eq!("abcba".is_palindrome(), true);
    /// ```
    fn is_palindrome(&self) -> bool {
        self.reverse() == self
    }

    /// 文字列を反転させる。
    ///
    /// # Examples
    ///
    /// ```
    /// use kyopro::MyString;
    ///
    /// assert_eq!("abc".reverse(), "cba");
    /// ```
    fn reverse(&self) -> String {
        self.chars().rev().collect()
    }

    /// 文字列を 1 桁ずつ数値に変換する。
    ///
    /// # Examples
    ///
    /// ```
    /// use kyopro::MyString;
    ///
    /// assert_eq!("7777".to_digits(), vec![7, 7, 7, 7]);
    /// assert_eq!("0112".to_digits(), vec![0, 1, 1, 2]);
    /// assert_eq!("9012".to_digits(), vec![9, 0, 1, 2]);
    /// ```
    fn to_digits(&self) -> Vec<u32> {
        self.chars().map(|c| c.to_digit(10).unwrap()).collect()
    }
}

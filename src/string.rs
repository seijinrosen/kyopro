pub trait MyString {
    fn is_palindrome(&self) -> bool;
    fn reverse(&self) -> String;
    fn to_digits(&self) -> Vec<u32>;
}

impl MyString for str {
    fn is_palindrome(&self) -> bool {
        self.reverse() == self
    }
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

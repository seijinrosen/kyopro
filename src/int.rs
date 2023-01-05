pub trait MyInt {
    fn is_even(&self) -> bool;
}

impl MyInt for i32 {
    /// 偶数かどうか。
    ///
    /// # Examples
    ///
    /// ```
    /// use kyopro::MyInt;
    ///
    /// assert_eq!(0.is_even(), true);
    /// assert_eq!(1.is_even(), false);
    /// ```
    fn is_even(&self) -> bool {
        self % 2 == 0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_even() {
        assert!(2.is_even());
        assert!(!3.is_even());
        assert!(4.is_even());
    }
}

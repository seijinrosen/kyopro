pub trait MyInt {
    fn is_even(&self) -> bool;
}

impl MyInt for i32 {
    fn is_even(&self) -> bool {
        self % 2 == 0
    }
}

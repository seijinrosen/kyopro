use proconio::input;

fn main() {
    input! {
        _n: i32,
        s: String,
    }

    let ans = s.dedup().len();

    println!("{}", ans);
}

pub trait MyString {
    fn dedup(&self) -> String;
}

impl MyString for str {
    fn dedup(&self) -> String {
        let mut vec = self.as_bytes().to_vec();
        vec.dedup();
        String::from_utf8(vec).unwrap()
    }
}

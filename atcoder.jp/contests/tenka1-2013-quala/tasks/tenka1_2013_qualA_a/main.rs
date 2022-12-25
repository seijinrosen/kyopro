fn main() {
    let mut x = 42;
    while x <= 130000000 {
        x *= 2;
    }

    println!("{}", x);
}

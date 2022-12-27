use proconio::input;

fn is_leap(y: i32) -> bool {
    match y {
        y if y % 400 == 0 => true,
        y if y % 100 == 0 => false,
        _ => y % 4 == 0,
    }
}

fn main() {
    input! {
        y: i32,
    }

    println!("{}", if is_leap(y) { "YES" } else { "NO" });
}

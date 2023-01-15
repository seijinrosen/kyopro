use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
    }

    let ans = a == b / 2;

    println!("{}", if ans { "Yes" } else { "No" });
}

use proconio::input;

fn main() {
    input! {
        (a, b): (i32, i32),
    }

    let ans = a.max(b);

    println!("{}", ans);
}

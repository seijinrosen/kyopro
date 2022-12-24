use proconio::input;

fn main() {
    input! {
        (a, b): (u32, u32),
    }

    let ans = a.pow(b);
    println!("{}", ans);
}

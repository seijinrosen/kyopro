use proconio::input;

fn main() {
    input! {
        a: String,
        b: String,
    }

    let ans = a.len() * b.len();

    println!("{}", ans);
}

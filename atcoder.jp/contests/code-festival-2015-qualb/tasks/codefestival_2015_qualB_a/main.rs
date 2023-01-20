use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = s.clone() + &s;

    println!("{}", ans);
}

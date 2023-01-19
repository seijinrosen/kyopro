use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let ans = s
        .chars()
        .zip("CODEFESTIVAL2016".chars())
        .fold(0, |acc, (ch1, ch2)| acc + (ch1 != ch2) as i32);

    println!("{}", ans);
}

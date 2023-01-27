use proconio::input;

fn main() {
    input! {
        c: String,
    }

    let ans = "OPKL".contains(&c);

    println!("{}", if ans { "Right" } else { "Left" });
}

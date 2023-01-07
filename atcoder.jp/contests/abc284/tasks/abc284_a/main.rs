use proconio::input;

fn main() {
    input! {
        n: usize,
        mut s: [String; n],
    }

    s.reverse();

    println!("{}", itertools::join(s, "\n"));
}

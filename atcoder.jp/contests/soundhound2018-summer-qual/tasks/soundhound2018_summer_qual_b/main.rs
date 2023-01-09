use proconio::input;

fn main() {
    input! {
        s: String,
        w: usize,
    }

    let mut ans = "".to_string();
    for (i, ch) in s.chars().enumerate() {
        if i % w == 0 {
            ans.push(ch);
        }
    }

    println!("{}", ans);
}

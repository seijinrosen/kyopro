use proconio::input;

fn main() {
    input! {
        n: usize,
        hs: [i32; n],
    }

    let ans = solve(0, &hs);

    println!("{}", ans);
}

fn solve(x: i32, hs: &[i32]) -> i32 {
    match hs {
        [] => 0,
        [h, hs @ ..] => {
            if x <= *h {
                solve(*h, hs) + 1
            } else {
                solve(x, hs)
            }
        }
    }
}

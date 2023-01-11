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
    if hs.is_empty() {
        return 0;
    }

    let h = hs[0];
    let hs = &hs[1..];

    if x <= h {
        return solve(h, hs) + 1;
    }

    solve(x, hs)
}

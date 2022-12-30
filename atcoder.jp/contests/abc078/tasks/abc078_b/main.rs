use proconio::input;

fn main() {
    input! {
        (x, y, z): (i32, i32, i32),
    }

    let ans = (x - z) / (y + z);

    println!("{}", ans);
}

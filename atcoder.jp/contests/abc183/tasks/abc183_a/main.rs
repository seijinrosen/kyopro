use proconio::input;

fn main() {
    input! {
        x: i32,
    }

    let ans = relu(x);

    println!("{}", ans);
}

fn relu(x: i32) -> i32 {
    if x >= 0 {
        return x;
    }
    0
}

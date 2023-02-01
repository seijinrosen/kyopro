use proconio::input;

fn main() {
    input! {
        mut a: usize,
        mut b: usize,
        k: usize,
    }

    for i in 0..k {
        if i % 2 == 0 {
            let (x, y) = func(a, b);
            a = x;
            b = y;
        } else {
            let (y, x) = func(b, a);
            a = x;
            b = y;
        }
    }

    println!("{} {}", a, b);
}

fn func(mut x: usize, mut y: usize) -> (usize, usize) {
    if x % 2 == 1 {
        x -= 1;
    }

    let tmp = x / 2;
    x -= tmp;
    y += tmp;

    (x, y)
}

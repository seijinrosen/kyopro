use proconio::input;

fn main() {
    input! {
        (a, b): (i32, i32),
    }

    let mut vec: Vec<i32> = Vec::new();

    if a < b {
        for i in 1..=b {
            vec.push(-i);
        }
        for i in 1..a {
            vec.push(i);
        }
    } else {
        for i in 1..=a {
            vec.push(i);
        }
        for i in 1..b {
            vec.push(-i);
        }
    }

    vec.push(-vec.iter().sum::<i32>());

    println!("{}", itertools::join(vec, " "))
}

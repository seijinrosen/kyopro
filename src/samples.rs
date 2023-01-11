// https://atcoder.jp/contests/abc124/tasks/abc124_b
fn recursive_pattern_match(x: i32, hs: &[i32]) -> i32 {
    match hs {
        [] => 0,
        [h, hs @ ..] => {
            if x <= *h {
                recursive_pattern_match(*h, hs) + 1
            } else {
                recursive_pattern_match(x, hs)
            }
        }
    }
}

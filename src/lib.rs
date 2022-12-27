/// うるう年かどうかを判定する。
///
/// # Examples
///
/// ```
/// use kyopro::is_leap;
///
/// assert_eq!(is_leap(1001), false);
/// assert_eq!(is_leap(2000), true);
/// assert_eq!(is_leap(2012), true);
/// assert_eq!(is_leap(2100), false);
/// ```
pub fn is_leap(year: i32) -> bool {
    match year {
        y if y % 400 == 0 => true,
        y if y % 100 == 0 => false,
        _ => year % 4 == 0,
    }
}

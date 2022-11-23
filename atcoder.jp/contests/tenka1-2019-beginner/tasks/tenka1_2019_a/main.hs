main :: IO ()
main = do
  [a, b, c] <- map read . words <$> getLine :: IO [Int]

  let ans = (a < c && c < b) || (b < c && c < a)
  putStrLn $ if ans then "Yes" else "No"

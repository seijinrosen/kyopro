main :: IO ()
main = do
  getLine
  as <- map read . words <$> getLine

  let ans = and [a `mod` 3 == 0 || a `mod` 5 == 0 | a <- as, even a]

  putStrLn $ if ans then "APPROVED" else "DENIED"

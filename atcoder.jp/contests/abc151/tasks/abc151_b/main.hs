main :: IO ()
main = do
  [n, k, m] <- map read . words <$> getLine
  a <- map read . words <$> getLine

  let x = n * m - sum a
      ans = if k < x then -1 else max x 0

  print ans

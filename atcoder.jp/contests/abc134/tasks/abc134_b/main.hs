main :: IO ()
main = do
  [n, d] <- map read . words <$> getLine
  let ans = ceiling $ n / (2 * d + 1)
  print ans

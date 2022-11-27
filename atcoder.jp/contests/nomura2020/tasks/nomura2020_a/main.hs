main :: IO ()
main = do
  [h1, m1, h2, m2, k] <- map read . words <$> getLine

  let ans = 60 * (h2 - h1) + m2 - m1 - k
  print ans

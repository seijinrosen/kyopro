main :: IO ()
main = do
  [m1, d1] <- map read . words <$> getLine
  [m2, d2] <- map read . words <$> getLine

  let ans = m2 - m1
  print ans

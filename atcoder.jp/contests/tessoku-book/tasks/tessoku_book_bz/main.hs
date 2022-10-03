main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine

  let ans = a + b
  print ans

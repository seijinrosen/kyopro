main :: IO ()
main = do
  [a, b, c, k] <- map read . words <$> getLine

  let a' = min a k
      b' = min b (k - a')
      c' = k - a' - b'
      ans = a' - c'

  print ans

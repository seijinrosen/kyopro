main :: IO ()
main = do
  [n, a, b] <- map read . words <$> getLine

  let b' = min 5 n
      a' = n - b'
      ans = a * a' + b * b'

  print ans

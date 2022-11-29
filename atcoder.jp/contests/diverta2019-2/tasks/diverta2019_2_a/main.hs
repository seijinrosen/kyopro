main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine

  let ans = if k == 1 then 0 else n - k
  print ans

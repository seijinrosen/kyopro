main :: IO ()
main = do
  [n, w] <- map read . words <$> getLine

  let ans = n `div` w

  print ans

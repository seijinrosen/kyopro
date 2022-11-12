main :: IO ()
main = do
  [l, r, d] <- map read . words <$> getLine

  let ans = r `div` d - (l - 1) `div` d
  print ans

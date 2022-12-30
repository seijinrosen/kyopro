main :: IO ()
main = do
  [x, y, z] <- map read . words <$> getLine

  let ans = (x - z) `div` (y + z)

  print ans

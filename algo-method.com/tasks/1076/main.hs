main :: IO ()
main = do
  getLine
  vs <- map read . words <$> getLine

  let ans = sum [2 ^ v | v <- vs]
  print ans

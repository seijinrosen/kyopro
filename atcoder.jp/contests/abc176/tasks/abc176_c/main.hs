main :: IO ()
main = do
  n <- readLn :: IO Int
  a <- map read . words <$> getLine

  let ans = sum $ zipWith (-) (scanl1 max a) a
  print ans

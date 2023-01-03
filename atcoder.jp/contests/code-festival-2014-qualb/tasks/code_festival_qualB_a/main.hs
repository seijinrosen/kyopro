main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine :: IO [Int]

  let ans = max a b

  print ans

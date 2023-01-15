main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine

  let ans = a == b `div` 2

  putStrLn $ if ans then "Yes" else "No"

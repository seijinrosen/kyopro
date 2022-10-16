main :: IO ()
main = do
  [k, x] <- map read . words <$> getLine
  let ans = [x - k + 1 .. x + k - 1]
  putStrLn . unwords $ map show ans

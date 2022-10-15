main :: IO ()
main = do
  n <- readLn :: IO Int
  a <- map read . words <$> getLine :: IO [Int]

  let ans = scanl1 max a
  mapM_ print ans

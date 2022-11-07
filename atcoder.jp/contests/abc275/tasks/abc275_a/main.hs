main :: IO ()
main = do
  n <- readLn :: IO Int
  h <- map read . words <$> getLine :: IO [Int]

  let ans = snd . maximum $ zip h [1 ..]
  print ans

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- map read . words <$> getLine

  let ans = maximum as - minimum as

  print ans

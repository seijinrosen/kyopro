main :: IO ()
main = do
  n <- readLn :: IO Int
  a <- getIntList
  b <- getIntList

  let ans = max 0 $ minimum b - maximum a + 1
  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

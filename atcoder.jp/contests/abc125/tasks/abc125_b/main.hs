getIntList :: IO [Int]
getIntList = map read . words <$> getLine

main :: IO ()
main = do
  n <- readLn :: IO Int
  vs <- getIntList
  cs <- getIntList

  let ans = sum $ zipWith (\v c -> max 0 (v - c)) vs cs
  print ans

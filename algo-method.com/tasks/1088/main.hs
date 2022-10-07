main :: IO ()
main = do
  [sa, ta] <- getIntList
  [sb, tb] <- getIntList

  let ans = max 0 $ min ta tb - max sa sb

  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

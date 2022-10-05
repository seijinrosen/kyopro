import Data.List (sort)

main :: IO ()
main = do
  [n, k] <- getIntList
  ps <- getIntList

  let ans = sum $ take k $ sort ps
  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

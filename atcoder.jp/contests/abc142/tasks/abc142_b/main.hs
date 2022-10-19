import Util (count)

main :: IO ()
main = do
  [n, k] <- getIntList
  h <- getIntList

  let ans = count (k <=) h
  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

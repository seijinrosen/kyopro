main :: IO ()
main = do
  [n, k] <- getIntList

  let ans = length [0 | a <- [1 .. n], b <- [1 .. n], let c = k - a - b, 1 <= c && c <= n]

  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

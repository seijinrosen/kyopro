main :: IO ()
main = do
  [n, d] <- getIntList
  let ans = n `divCeil` (2 * d + 1)
  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

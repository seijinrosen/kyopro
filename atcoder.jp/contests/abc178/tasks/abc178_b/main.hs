getIntList :: IO [Int]
getIntList = map read . words <$> getLine

main :: IO ()
main = do
  [a, b, c, d] <- getIntList

  let ans = maximum [x * y | x <- [a, b], y <- [c, d]]
  print ans

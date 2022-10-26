import Util (count)

main :: IO ()
main = do
  n <- readLn :: IO Int
  p <- getIntList

  let ans = count (\(a, b, c) -> (a < b && b < c) || (c < b && b < a)) $ zip3 p (tail p) (tail $ tail p)
  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

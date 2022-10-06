main :: IO ()
main = do
  [n, y] <- getIntList

  let candidates = [[i, j, k] | i <- [0 .. n], j <- [0 .. n - i], let k = n - i - j, 10000 * i + 5000 * j + 1000 * k == y]
      ans = if null candidates then [-1, -1, -1] else head candidates

  putStrLn $ showIntList ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

showIntList :: [Int] -> String
showIntList = unwords . map show

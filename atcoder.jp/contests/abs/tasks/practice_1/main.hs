main :: IO ()
main = do
  a <- getInt
  [b, c] <- getIntList
  s <- getLine

  let ans = a + b + c
  putStrLn $ show ans ++ " " ++ s

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

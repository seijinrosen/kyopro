main :: IO ()
main = do
  [a, b] <- getIntList

  let ans = evenOdd $ a * b
  putStrLn ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

evenOdd :: Int -> String
evenOdd x = if odd x then "Odd" else "Even"

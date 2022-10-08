import Data.Char (intToDigit)

main :: IO ()
main = do
  [a, b] <- getIntList

  let ans = min (replicate b . intToDigit $ a) (replicate a . intToDigit $ b)

  putStrLn ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

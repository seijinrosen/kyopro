import Data.Char (digitToInt)

main :: IO ()
main = do
  [n, a, b] <- getIntList

  let ans = sum [i | i <- [1 .. n], a <= sumOfEachDigit i, sumOfEachDigit i <= b]
  print ans

-- input functions

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions

sumOfEachDigit :: Int -> Int
sumOfEachDigit i = sum $ map digitToInt $ show i

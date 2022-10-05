main :: IO ()
main = do
  n <- getInt
  as <- getIntList

  let ans = minimum $ map primeFactor2 as
  print ans

-- input functions

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions

primeFactor2 :: Int -> Int
primeFactor2 n
  | odd n = 0
  | otherwise = primeFactor2 (n `div` 2) + 1

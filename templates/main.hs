main :: IO ()
main = do
  n <- getInt
  [a, b] <- getIntList

  let ans = a + b

  print ans

-- input functions
getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions
isDivisorOf100 :: Int -> Bool
isDivisorOf100 x = 100 `mod` x == 0

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

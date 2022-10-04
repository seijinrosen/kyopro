main :: IO ()
main = do
  n <- getInt
  [a, b] <- getIntList
  ps <- getIntList

  let ans = a `elem` ps

  print ans
  putStrLn $ yesNo ans

-- input functions
getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions
isDivisorOf100 :: Int -> Bool
isDivisorOf100 x = 100 `mod` x == 0

itertoolsProduct :: [a] -> [b] -> [(a, b)]
itertoolsProduct ps qs = [(p, q) | p <- ps, q <- qs]

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

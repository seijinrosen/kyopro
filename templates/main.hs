import Control.Monad (replicateM)
import Data.Char (digitToInt)

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

getVerticalIntList :: Int -> IO [Int]
getVerticalIntList n = replicateM n getInt

-- functions

-- https://wiki.haskell.jp/Old/sampou.org/Programming_玉手箱#組合せの生成
combinations :: [a] -> Int -> [[a]]
combinations _ 0 = [[]]
combinations [] _ = []
combinations (x : xs) n = map (x :) (combinations xs (n - 1)) ++ combinations xs n

count :: Eq a => a -> [a] -> Int
count x s = length $ filter (== x) s

evenOdd :: Int -> String
evenOdd x = if odd x then "Odd" else "Even"

isDivisorOf100 :: Int -> Bool
isDivisorOf100 x = 100 `mod` x == 0

itertoolsProduct :: [a] -> [b] -> [(a, b)]
itertoolsProduct ps qs = [(p, q) | p <- ps, q <- qs]

primeFactor2 :: Int -> Int
primeFactor2 n
  | odd n = 0
  | otherwise = primeFactor2 (n `div` 2) + 1

step2 :: [a] -> [a]
step2 [] = []
step2 [x] = [x]
step2 (x : y : xs) = x : step2 xs

sumOfEachDigit :: Int -> Int
sumOfEachDigit i = sum $ map digitToInt $ show i

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

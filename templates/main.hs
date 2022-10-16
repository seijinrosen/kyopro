import Control.Monad (replicateM)
import Data.Char (digitToInt, intToDigit)
import Data.Function ((&))
import Data.List (find, isPrefixOf, stripPrefix)
import qualified Data.Map as Map

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- map read . words <$> getLine :: IO [Int]
  [a, b] <- getIntList
  ps <- getIntList

  let ans = a `elem` ps
  let acc = scanl1 max as

  print ans
  putStrLn $ yesNo ans

-- input functions

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

getIntListList :: Int -> IO [[Int]]
getIntListList n = replicateM n getIntList

getVerticalIntList :: Int -> IO [Int]
getVerticalIntList n = replicateM n getInt

toPair :: [Int] -> (Int, Int)
toPair [p, q] = (p, q)
toPair _ = (0, 0)

getIntPair :: IO (Int, Int)
getIntPair = toPair . map read . words <$> getLine

getIntPairList :: Int -> IO [(Int, Int)]
getIntPairList n = replicateM n getIntPair

type Tuple = (Int, Int, Int, Int)

toTuple :: [Int] -> Tuple
toTuple [p, q, r, s] = (p, q, r, s)
toTuple _ = (0, 0, 0, 0)

getIntTuple :: IO Tuple
getIntTuple = toTuple . map read . words <$> getLine

getIntTupleList :: Int -> IO [Tuple]
getIntTupleList n = replicateM n getIntTuple

-- print functions

printVertically :: (Foldable t, Show a) => t a -> IO ()
printVertically = mapM_ print

putStrLnVertically :: [String] -> IO ()
putStrLnVertically = mapM_ putStrLn

-- functions

accumulate :: [Int] -> [Int]
accumulate [] = []
accumulate [x] = [x]
accumulate (x : y : xs) = x : accumulate (x + y : xs)

accumulateMax :: [Int] -> [Int]
accumulateMax [] = []
accumulateMax [x] = [x]
accumulateMax (x : y : xs) = x : accumulateMax (max x y : xs)

bin2int :: String -> Int
bin2int b = sum [2 ^ i | (i, c) <- enumerate $ reverse b, c == '1']

-- https://wiki.haskell.jp/Old/sampou.org/Programming_玉手箱#組合せの生成
combinations :: [a] -> Int -> [[a]]
combinations _ 0 = [[]]
combinations [] _ = []
combinations (x : xs) n = map (x :) (combinations xs (n - 1)) ++ combinations xs n

count :: Eq a => a -> [a] -> Int
count x = length . filter (== x)

counter :: (Ord k, Num a) => [k] -> Map.Map k a
counter xs = Map.fromListWith (+) $ zip xs (repeat 1)

enumerate :: [b] -> [(Int, b)]
enumerate = zip [0 ..]

evenOdd :: Int -> String
evenOdd x = if odd x then "Odd" else "Even"

findPrefix :: String -> [String] -> Maybe String
findPrefix s = find (`isPrefixOf` s)

int2bin :: Int -> String
int2bin 0 = "0"
int2bin 1 = "1"
int2bin num = int2bin (num `div` 2) ++ [intToDigit $ num `mod` 2]

isDivisorOf100 :: Int -> Bool
isDivisorOf100 x = 100 `mod` x == 0

isLeapYear :: Int -> Bool
isLeapYear n
  | n `mod` 400 == 0 = True
  | n `mod` 100 == 0 = False
  | n `mod` 4 == 0 = True
  | otherwise = False

itertoolsProduct :: [a] -> [b] -> [(a, b)]
itertoolsProduct ps qs = [(p, q) | p <- ps, q <- qs]

pairwise :: [b] -> [(b, b)]
pairwise iterable = zip iterable $ tail iterable

primeFactor2 :: Int -> Int
primeFactor2 n
  | odd n = 0
  | otherwise = primeFactor2 (n `div` 2) + 1

showIntList :: [Int] -> String
showIntList = unwords . map show

step2 :: [a] -> [a]
step2 [] = []
step2 [x] = [x]
step2 (x : y : xs) = x : step2 xs

stripPrefixFromList :: [String] -> String -> Maybe String
stripPrefixFromList [] _ = Nothing
stripPrefixFromList (prefix : prefixes) s = case stripPrefix prefix s of
  Just x -> Just x
  Nothing -> stripPrefixFromList prefixes s

sumOfEachDigit :: Int -> Int
sumOfEachDigit i = sum $ map digitToInt $ show i

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

zfill :: Int -> String -> String
zfill width s
  | diff <= 0 = s
  | otherwise = replicate diff '0' ++ s
  where
    diff = width - length s

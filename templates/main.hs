import Control.Monad (replicateM)
import Data.Char (digitToInt, intToDigit)
import Data.Function ((&))
import Data.List (find, findIndices, isPrefixOf, stripPrefix)
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Maybe (fromMaybe)
import Data.Set (Set)
import qualified Data.Set as Set
import qualified Data.Text as T
import Util (count)

solve :: String -> Bool
solve s = True

main :: IO ()
main = do
  n <- readLn :: IO Int
  as <- map read . words <$> getLine :: IO [Int]
  [a, b] <- getIntList
  ps <- getIntList
  -- st <- replicateM n $ do
  --   [s, t] <- words <$> getLine
  --   return (s, read t)

  let ans = a `elem` ps
  -- let acc = scanl1 max as

  print ans
  putStrLn $ yesNo ans
  getLine >>= putStrLn . yesNo . solve
  putStrLn $ if ans then "Yes" else "No"

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

printList :: Show a => [a] -> IO ()
printList = putStrLn . unwords . map show

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

countText :: String -> String -> Int
countText s = T.count (T.pack s) . T.pack

counter :: (Ord k, Num a) => [k] -> Map k a
counter xs = Map.fromListWith (+) $ zip xs (repeat 1)

dedup :: Eq a => [a] -> [a]
dedup [] = []
dedup [x] = [x]
dedup (x : y : xs) =
  if x == y
    then dedup (y : xs)
    else x : dedup (y : xs)

divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

enumerate :: [b] -> [(Int, b)]
enumerate = zip [0 ..]

evenOdd :: Int -> String
evenOdd x = if odd x then "Odd" else "Even"

findIndexR :: (a -> Bool) -> [a] -> Int
findIndexR p xs
  | null indices = -1
  | otherwise = last indices
  where
    indices = findIndices p xs

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

isPalindrome :: Eq a => [a] -> Bool
isPalindrome s = reverse s == s

itertoolsProduct :: [a] -> [b] -> [(a, b)]
itertoolsProduct ps qs = [(p, q) | p <- ps, q <- qs]

lstrip :: Eq a => a -> [a] -> [a]
lstrip c = dropWhile (== c)

pairwise :: [b] -> [(b, b)]
pairwise iterable = zip iterable $ tail iterable

primeFactor2 :: Int -> Int
primeFactor2 n
  | odd n = 0
  | otherwise = primeFactor2 (n `div` 2) + 1

readIntAtBase :: Int -> String -> Int
readIntAtBase k s = sum [k ^ i * digitToInt c | (i, c) <- zip [0 ..] $ reverse s]

repeatStr :: Int -> [a] -> [a]
repeatStr n = concat . replicate n

rstrip :: Eq a => a -> [a] -> [a]
rstrip c = reverse . dropWhile (== c) . reverse

showIntList :: [Int] -> String
showIntList = unwords . map show

showPair :: (Show a1, Show a2) => (a1, a2) -> String
showPair p = show (fst p) ++ " " ++ show (snd p)

slice :: Int -> Int -> [a] -> [a]
slice start end = drop start . take end

step2 :: [a] -> [a]
step2 [] = []
step2 [x] = [x]
step2 (x : y : xs) = x : step2 xs

stripPrefixFromList :: [String] -> String -> Maybe String
stripPrefixFromList [] _ = Nothing
stripPrefixFromList (prefix : prefixes) s = case stripPrefix prefix s of
  Just x -> Just x
  Nothing -> stripPrefixFromList prefixes s

substr :: Int -> Int -> [a] -> [a]
substr start len = take len . drop start

sumOfEachDigit :: Int -> Int
sumOfEachDigit i = sum $ map digitToInt $ show i

symmetricDifference :: Ord a => Set a -> Set a -> Set a
symmetricDifference s1 s2 = Set.union s1 s2 `Set.difference` Set.intersection s1 s2

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

translate :: Ord k => Map k k -> k -> k
translate mp x = fromMaybe x $ Map.lookup x mp

uniqLen :: Ord a => [a] -> Int
uniqLen = length . Set.fromList

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

zfill :: Int -> String -> String
zfill width s
  | diff <= 0 = s
  | otherwise = replicate diff '0' ++ s
  where
    diff = width - length s

-- misc

cond2 :: String -> Bool
cond2 s = case reads s of
  [(n, _)] -> 100000 <= n && n <= 999999
  _ -> False

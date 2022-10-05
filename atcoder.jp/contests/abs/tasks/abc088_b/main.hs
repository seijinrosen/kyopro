import Data.List (sort)

main :: IO ()
main = do
  n <- getInt
  a <- getIntList

  let sortedA = reverse . sort $ a
      alice = sum . step2 $ sortedA
      bob = sum . step2 . tail $ sortedA
      ans = alice - bob

  print ans

-- input functions

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions

step2 :: [a] -> [a]
step2 [] = []
step2 [x] = [x]
step2 (x : y : xs) = x : step2 xs

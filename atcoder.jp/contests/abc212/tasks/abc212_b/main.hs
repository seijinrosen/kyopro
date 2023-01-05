import Data.Char (digitToInt)
import qualified Data.Set as Set

isWeak1 :: [Int] -> Bool
isWeak1 = (== 1) . Set.size . Set.fromList

isWeak2 :: [Int] -> Bool
isWeak2 [] = True
isWeak2 [_] = True
isWeak2 (x : y : xs) = (x + 1) `mod` 10 == y && isWeak2 (y : xs)

main :: IO ()
main = do
  xs <- map digitToInt <$> getLine

  putStrLn $
    if isWeak1 xs || isWeak2 xs
      then "Weak"
      else "Strong"

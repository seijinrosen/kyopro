import Data.List (sortOn)
import qualified Data.Ord
import qualified Data.Vector as Vector

main :: IO ()
main = do
  n <- getLine
  a <- map read . words <$> getLine

  let ans = solve a
  print ans

solve :: [Int] -> Int
solve xs = fst $ vec Vector.! 1
  where
    sorted = sortOn (Data.Ord.Down . snd) $ zip [1 ..] xs
    vec = Vector.fromList sorted

import Data.Set (Set)
import qualified Data.Set as Set

symmetricDifference :: Ord a => Set a -> Set a -> Set a
symmetricDifference s1 s2 = Set.union s1 s2 `Set.difference` Set.intersection s1 s2

solve :: [Int] -> [Int] -> [Int]
solve a b = Set.toAscList $ symmetricDifference (Set.fromList a) (Set.fromList b)

main :: IO ()
main = do
  getLine
  a <- map read . words <$> getLine
  b <- map read . words <$> getLine

  printList $ solve a b

printList :: Show a => [a] -> IO ()
printList = putStrLn . unwords . map show

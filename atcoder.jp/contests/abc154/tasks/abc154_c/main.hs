import qualified Data.Set as Set

uniqLen :: Ord a => [a] -> Int
uniqLen = length . Set.fromList

main :: IO ()
main = do
  n <- readLn
  a <- map read . words <$> getLine :: IO [Int]

  let ans = uniqLen a == n

  putStrLn $ if ans then "YES" else "NO"

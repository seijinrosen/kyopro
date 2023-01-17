import Control.Monad (replicateM)
import qualified Data.Set as Set

main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine
  as <- replicateM k $ do
    d <- getLine
    map read . words <$> getLine :: IO [Int]

  let ans = n - length (Set.fromList [v | a <- as, v <- a])

  print ans

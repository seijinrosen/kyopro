import Control.Monad (replicateM)
import qualified Data.Map as Map

main :: IO ()
main = do
  n <- readLn
  s <- replicateM n getLine

  let ans = solve s

  mapM_ putStrLn ans

solve :: [String] -> [String]
solve s = [r ++ " x " ++ maybe "0" show (Map.lookup r c) | r <- results]
  where
    c = counter s

results :: [String]
results = ["AC", "WA", "TLE", "RE"]

counter :: (Ord k, Num a) => [k] -> Map.Map k a
counter xs = Map.fromListWith (+) $ zip xs (repeat 1)

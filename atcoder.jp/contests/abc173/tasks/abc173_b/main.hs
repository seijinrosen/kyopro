import Control.Monad (replicateM)

main :: IO ()
main = do
  n <- readLn
  s <- replicateM n getLine

  let ans = [r ++ " x " ++ show (count r s) | r <- ["AC", "WA", "TLE", "RE"]]

  mapM_ putStrLn ans

count :: Eq a => a -> [a] -> Int
count x s = length $ filter (== x) s

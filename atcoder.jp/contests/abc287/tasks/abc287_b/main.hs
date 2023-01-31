import Control.Monad (replicateM)

main :: IO ()
main = do
  [n, m] <- map read . words <$> getLine
  s <- replicateM n getLine
  t <- replicateM m getLine

  let ans = length [() | s <- s, drop 3 s `elem` t]

  print ans

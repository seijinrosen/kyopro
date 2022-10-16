import Control.Monad (replicateM)

main :: IO ()
main = do
  [h, w] <- map read . words <$> getLine
  s <- replicateM h getLine

  let ans = sum $ map (count 'o') s
  print ans

count :: Eq a => a -> [a] -> Int
count x = length . filter (== x)

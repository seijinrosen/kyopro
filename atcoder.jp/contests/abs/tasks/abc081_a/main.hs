main :: IO ()
main = do
  s <- getLine

  let ans = count '1' s
  print ans

count :: Eq a => a -> [a] -> Int
count x s = length $ filter (== x) s

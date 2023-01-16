solve :: (Num p, Eq a) => [a] -> [a] -> p
solve _ [] = 0
solve [] _ = 0
solve (x : xs) (y : ys)
  | x == y = 0
  | otherwise = solve xs ys + 1

main :: IO ()
main = do
  n <- readLn
  s <- getLine

  let ans = [solve s (drop i s) | i <- [1 .. n - 1]]

  mapM_ print ans

solve :: (Ord a1, Ord a2, Num a2, Num a1) => a1 -> a1 -> a1 -> a2 -> Bool
solve a b c k
  | a < b && b < c = True
  | k <= 0 = False
  | a >= b = solve a (b * 2) c (k - 1)
  | b >= c = solve a b (c * 2) (k - 1)
  | otherwise = solve a b c (k - 1)

main :: IO ()
main = do
  [a, b, c] <- map read . words <$> getLine
  k <- readLn

  let ans = solve a b c k

  putStrLn $ if ans then "Yes" else "No"

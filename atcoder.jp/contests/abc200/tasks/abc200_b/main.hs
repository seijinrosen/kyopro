func :: Integral a => a -> a
func n
  | n `mod` 200 == 0 = n `div` 200
  | otherwise = 1000 * n + 200

main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine

  let ans = foldl (\a _ -> func a) n [1 .. k]
  print ans

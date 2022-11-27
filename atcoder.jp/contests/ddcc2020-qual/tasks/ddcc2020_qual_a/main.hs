prize :: Int -> Int
prize n = case n of
  3 -> 100000
  2 -> 200000
  1 -> 300000
  _ -> 0

additionalPrize :: Int -> Int -> Int
additionalPrize x y
  | x == 1 && y == 1 = 400000
  | otherwise = 0

main :: IO ()
main = do
  [x, y] <- map read . words <$> getLine

  let ans = prize x + prize y + additionalPrize x y
  print ans

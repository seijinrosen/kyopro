solve :: Int -> Int -> Int -> Ordering
solve a b c
  | even c = abs a `compare` abs b
  | otherwise = a `compare` b

orderingToChar :: Ordering -> Char
orderingToChar LT = '<'
orderingToChar EQ = '='
orderingToChar GT = '>'

main :: IO ()
main = do
  [a, b, c] <- map read . words <$> getLine

  let ans = solve a b c
  putStrLn [orderingToChar ans]

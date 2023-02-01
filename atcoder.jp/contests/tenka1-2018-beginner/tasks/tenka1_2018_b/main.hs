solve :: Int -> Int -> Int -> Int -> (Int, Int)
solve a b k now
  | now == k = (a, b)
  | otherwise =
    if even now
      then solve (a `div` 2) (b + a `div` 2) k (now + 1)
      else solve (a + b `div` 2) (b `div` 2) k (now + 1)

main :: IO ()
main = do
  [a, b, k] <- map read . words <$> getLine

  let ans = solve a b k 0

  putStrLn $ showPair ans

showPair :: (Show a1, Show a2) => (a1, a2) -> String
showPair p = show (fst p) ++ " " ++ show (snd p)

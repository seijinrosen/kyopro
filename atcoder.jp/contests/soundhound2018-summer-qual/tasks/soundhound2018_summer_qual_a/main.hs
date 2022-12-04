solve :: Int -> Int -> String
solve a b
  | a + b == 15 = "+"
  | a * b == 15 = "*"
  | otherwise = "x"

main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine
  putStrLn $ solve a b

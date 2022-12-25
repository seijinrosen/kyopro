solve :: Int -> Int -> Int
solve x y
  | x < y = y
  | otherwise = solve x (y * 2)

main :: IO ()
main = print $ solve 130000000 42

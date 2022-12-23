solve :: Int -> Int -> [Int]
solve a b = lst ++ [- sum lst]
  where
    lst
      | a < b = [-1, -2 .. - b] ++ [1 .. a - 1]
      | otherwise = [1 .. a] ++ [-1, -2 .. 1 - b]

main :: IO ()
main = do
  interact $ unwords . map show . (\[a, b] -> solve a b) . map read . words

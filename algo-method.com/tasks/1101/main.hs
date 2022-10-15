main :: IO ()
main = do
  n <- getLine
  a <- map read . words <$> getLine

  let ans = accumulateMax a
  mapM_ print ans

accumulateMax :: [Int] -> [Int]
accumulateMax [] = []
accumulateMax [x] = [x]
accumulateMax (x : y : xs) = x : accumulateMax (max x y : xs)

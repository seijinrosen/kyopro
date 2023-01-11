solve :: Ord t => t -> [t] -> Int
solve _ [] = 0
solve x (h : hs) =
  if x <= h
    then solve h hs + 1
    else solve x hs

main :: IO ()
main = do
  n <- readLn :: IO Int
  hs <- map read . words <$> getLine

  let ans = solve 0 hs

  print ans

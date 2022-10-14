import Data.List (sort)

main :: IO ()
main = do
  n <- readLn
  a <- map (read :: String -> Int) . words <$> getLine

  let ans = sort a !! (n - 2)
  print ans

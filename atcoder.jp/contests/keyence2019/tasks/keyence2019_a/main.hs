import Data.List (sort)

main :: IO ()
main = do
  n <- concat . words <$> getLine

  let ans = sort n == sort "1974"
  putStrLn $ if ans then "YES" else "NO"

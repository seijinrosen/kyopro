import Data.List (sort)

main :: IO ()
main = do
  [n, k] <- map read . words <$> getLine
  hs <- map read . words <$> getLine

  let ans = sum . drop k . reverse . sort $ hs

  print ans

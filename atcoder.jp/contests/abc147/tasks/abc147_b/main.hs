import Data.Function ((&))

main :: IO ()
main = do
  s <- getLine
  let ans = s & zip (reverse s) & filter (uncurry (/=)) & length & flip div 2
  print ans

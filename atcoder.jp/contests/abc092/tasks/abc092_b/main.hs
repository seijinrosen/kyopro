import Control.Monad (replicateM)

divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

main :: IO ()
main = do
  n <- readLn
  [d, x] <- map read . words <$> getLine
  a <- replicateM n readLn

  let ans = x + sum (map (d `divCeil`) a)
  print ans

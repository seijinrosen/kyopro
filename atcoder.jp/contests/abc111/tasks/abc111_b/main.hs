divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

main :: IO ()
main = do
  n <- readLn

  let ans = n `divCeil` 111 * 111
  print ans

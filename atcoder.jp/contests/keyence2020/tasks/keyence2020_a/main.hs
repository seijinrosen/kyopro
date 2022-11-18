divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

main :: IO ()
main = do
  h <- readLn
  w <- readLn
  n <- readLn

  let ans = n `divCeil` max h w
  print ans

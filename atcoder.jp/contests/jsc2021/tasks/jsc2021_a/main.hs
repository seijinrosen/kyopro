divCeil :: Integral a => a -> a -> a
a `divCeil` b = (a + b - 1) `div` b

main :: IO ()
main = do
  [x, y, z] <- map read . words <$> getLine
  print $ divCeil (y * z) x - 1

main :: IO ()
main = do
  [r, d, x2000] <- map read . words <$> getLine
  let ans = tail . take 11 $ iterate (\x -> r * x - d) x2000
  mapM_ print ans

main :: IO ()
main = do
  [s, t] <- map read . words <$> getLine

  let ans = length [() | a <- [0 .. s], b <- [0 .. s - a], c <- [0 .. s - a - b], a * b * c <= t]

  print ans

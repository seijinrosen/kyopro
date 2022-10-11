main :: IO ()
main = do
  n <- readLn
  print $ sum [i | i <- [1 .. n], i `mod` 3 /= 0, i `mod` 5 /= 0]

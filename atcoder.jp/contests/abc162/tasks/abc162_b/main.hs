main :: IO ()
main = do
  n <- readLn
  print $ sum [i | i <- take n [1 ..], i `mod` 3 /= 0, i `mod` 5 /= 0]

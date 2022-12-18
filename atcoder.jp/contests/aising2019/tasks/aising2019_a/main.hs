main :: IO ()
main = do
  n <- readLn
  h <- readLn
  w <- readLn

  let h' = n - h + 1
      w' = n - w + 1
      ans = h' * w'

  print ans

main :: IO ()
main = do
  n <- readLn

  let ans = (n - 1) `div` 2
  print ans

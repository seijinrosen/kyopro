main :: IO ()
main = do
  n <- readLn

  let ans = n * n
  print ans

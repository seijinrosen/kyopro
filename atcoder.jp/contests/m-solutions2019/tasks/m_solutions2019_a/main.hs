main :: IO ()
main = do
  n <- readLn

  let ans = 180 * (n - 2)
  print ans

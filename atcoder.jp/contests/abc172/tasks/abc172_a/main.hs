main :: IO ()
main = do
  a <- readLn

  let ans = a + a ^ 2 + a ^ 3

  print ans

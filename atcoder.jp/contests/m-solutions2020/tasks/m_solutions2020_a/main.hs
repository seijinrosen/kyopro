main :: IO ()
main = do
  x <- readLn

  let ans = 10 - x `div` 200
  print ans

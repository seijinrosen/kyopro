main :: IO ()
main = do
  a <- getLine
  b <- getLine

  let ans = length a * length b
  print ans

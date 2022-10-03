main :: IO ()
main = do
  n <- readLn
  [a, b] <- map read . words <$> getLine
  p <- map read . words <$> getLine

  let ans = n * n
  let ans = a + b
  print ans
  putStrLn $ map toLowerAlphabet p

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

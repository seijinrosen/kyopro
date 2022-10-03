main :: IO ()
main = do
  n <- readLn
  p <- map read . words <$> getLine

  let ans = n * n
  print ans
  putStrLn $ map toLowerAlphabet p

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

main :: IO ()
main = do
  p <- map read . words <$> getLine
  putStrLn $ map toLowerAlphabet p

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

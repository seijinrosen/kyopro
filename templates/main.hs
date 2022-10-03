main :: IO ()
main = do
  n <- readLn
  [a, b] <- map read . words <$> getLine
  [n, x] <- words <$> getLine
  a <- words <$> getLine
  p <- map read . words <$> getLine

  let ans = n * n
  let ans = a + b
  print ans
  let ans = x `elem` a
  putStrLn $ yesNo ans
  putStrLn $ map toLowerAlphabet p

toLowerAlphabet :: Int -> Char
toLowerAlphabet x = ['a' .. 'z'] !! (x - 1)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

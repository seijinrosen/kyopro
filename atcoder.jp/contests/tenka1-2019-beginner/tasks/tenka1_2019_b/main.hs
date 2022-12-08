func :: Char -> Char -> Char
func sk c
  | c == sk = c
  | otherwise = '*'

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- getLine
  k <- readLn

  let sk = s !! (k - 1)
      ans = map (func sk) s
  putStrLn ans

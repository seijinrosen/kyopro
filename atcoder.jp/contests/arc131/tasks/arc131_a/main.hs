main :: IO ()
main = do
  a <- getLine
  b <- readLn

  let x = show (b * 5) ++ a
  putStrLn x

main :: IO ()
main = do
  s <- getLine

  let ans = take 3 s
  putStrLn ans

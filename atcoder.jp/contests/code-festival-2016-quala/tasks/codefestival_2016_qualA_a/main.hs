main :: IO ()
main = do
  s <- getLine

  let ans = take 4 s ++ " " ++ drop 4 s

  putStrLn ans

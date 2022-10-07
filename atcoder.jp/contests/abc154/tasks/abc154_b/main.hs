main :: IO ()
main = do
  s <- getLine

  let ans = replicate (length s) 'x'

  putStrLn ans

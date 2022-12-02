main :: IO ()
main = do
  s <- getLine

  let ans = if length s == 2 then s else reverse s
  putStrLn ans

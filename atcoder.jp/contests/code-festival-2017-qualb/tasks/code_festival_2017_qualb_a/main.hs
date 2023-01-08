substr :: Int -> Int -> [a] -> [a]
substr start len = take len . drop start

main :: IO ()
main = do
  s <- getLine

  let ans = substr 0 (length s - 8) s

  putStrLn ans

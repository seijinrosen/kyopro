main :: IO ()
main = do
  c <- getLine

  let ans = head c `elem` "OPKL"

  putStrLn $ if ans then "Right" else "Left"

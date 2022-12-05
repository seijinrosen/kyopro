import Util (count)

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- getLine

  let ans = count (== 'B') s < count (== 'R') s
  putStrLn $ if ans then "Yes" else "No"

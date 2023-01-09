solve :: Int -> [a] -> [a]
solve _ [] = []
solve w (x : xs) = x : solve w (drop (w - 1) xs)

main :: IO ()
main = do
  s <- getLine
  w <- readLn

  let ans = solve w s

  putStrLn ans

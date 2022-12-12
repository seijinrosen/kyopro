main :: IO ()
main = do
  n <- readLn
  mapM_ print [n, n - 1 .. 0]

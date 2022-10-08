main :: IO ()
main = do
  k <- readLn
  s <- getLine

  let ans =
        if length s <= k
          then s
          else take k s ++ "..."

  putStrLn ans

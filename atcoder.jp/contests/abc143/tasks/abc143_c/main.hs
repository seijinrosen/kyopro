dedup :: Eq a => [a] -> [a]
dedup [] = []
dedup [x] = [x]
dedup (x : y : xs) =
  if x == y
    then dedup (y : xs)
    else x : dedup (y : xs)

main :: IO ()
main = do
  n <- readLn :: IO Int
  s <- getLine

  let ans = length . dedup $ s

  print ans

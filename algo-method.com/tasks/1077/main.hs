main :: IO ()
main = do
  n <- getInt

  let ans = 2 ^ n - 1
  print ans

getInt :: IO Int
getInt = readLn

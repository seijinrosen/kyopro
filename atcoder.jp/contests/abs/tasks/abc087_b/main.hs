main :: IO ()
main = do
  a <- getInt
  b <- getInt
  c <- getInt
  x <- getInt

  let ans = length [0 | i <- [0 .. a], j <- [0 .. b], k <- [0 .. c], 500 * i + 100 * j + 50 * k == x]
  print ans

getInt :: IO Int
getInt = readLn

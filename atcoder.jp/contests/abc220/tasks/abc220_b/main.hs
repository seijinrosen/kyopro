import Data.Char (digitToInt)

readIntAtBase :: Int -> String -> Int
readIntAtBase k s = sum [k ^ i * digitToInt c | (i, c) <- zip [0 ..] $ reverse s]

main :: IO ()
main = do
  k <- readLn
  [a, b] <- map (readIntAtBase k) . words <$> getLine

  let ans = a * b
  print ans

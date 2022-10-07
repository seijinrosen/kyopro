main :: IO ()
main = do
  n <- getLine

  let ans = bin2int n

  print ans

-- functions

bin2int :: String -> Int
bin2int b = sum [2 ^ i | (i, c) <- enumerate $ reverse b, c == '1']

enumerate :: [b] -> [(Int, b)]
enumerate = zip [0 ..]

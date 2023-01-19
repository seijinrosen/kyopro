solve :: String -> Int
solve s = length [() | (ch1, ch2) <- zip s "CODEFESTIVAL2016", ch1 /= ch2]

main :: IO ()
main = do
  getLine >>= print . solve

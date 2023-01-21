slice :: Int -> Int -> [a] -> [a]
slice start end = drop start . take end

main :: IO ()
main = do
  [n, p, q, r, s] <- map read . words <$> getLine
  as <- map read . words <$> getLine :: IO [Int]

  let a = slice 0 (p - 1) as
      b = slice (r - 1) s as
      c = slice q (r - 1) as
      d = slice (p - 1) q as
      e = slice s n as
      ans = a ++ b ++ c ++ d ++ e

  printList ans

printList :: Show a => [a] -> IO ()
printList = putStrLn . unwords . map show

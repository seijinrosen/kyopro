import Data.Set (difference, fromList, toList)

main :: IO ()
main = do
  s1 <- getLine
  s2 <- getLine
  s3 <- getLine

  let s = fromList [s1, s2, s3]
      contests = fromList ["ABC", "ARC", "AGC", "AHC"]
      ans = contests `difference` s

  putStrLn $ head . toList $ ans

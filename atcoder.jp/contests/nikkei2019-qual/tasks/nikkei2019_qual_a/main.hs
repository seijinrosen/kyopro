printList :: Show a => [a] -> IO ()
printList = putStrLn . unwords . map show

main :: IO ()
main = do
  [n, a, b] <- map read . words <$> getLine
  printList [min a b, max 0 (a + b - n)]

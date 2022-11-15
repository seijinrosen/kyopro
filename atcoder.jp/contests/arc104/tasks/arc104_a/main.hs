showIntList :: [Int] -> String
showIntList = unwords . map show

main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine

  let x = (a + b) `div` 2
      y = (a - b) `div` 2

  putStrLn $ showIntList [x, y]

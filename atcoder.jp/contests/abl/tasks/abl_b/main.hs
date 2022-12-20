printYesNo :: Bool -> IO ()
printYesNo False = putStrLn "No"
printYesNo True = putStrLn "Yes"

main :: IO ()
main = do
  [a, b, c, d] <- map read . words <$> getLine :: IO [Int]
  printYesNo $ max a c <= min b d

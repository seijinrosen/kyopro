main :: IO ()
main = do
  [n, x] <- words <$> getLine
  a <- words <$> getLine

  let ans = x `elem` a
  putStrLn $ yesNo ans

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

main :: IO ()
main = do
  [h, n] <- getIntList
  a <- getIntList

  let ans = h <= sum a
  putStrLn $ yesNo ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

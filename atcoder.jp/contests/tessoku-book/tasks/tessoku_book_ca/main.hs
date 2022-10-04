main :: IO ()
main = do
  [a, b] <- getIntList

  let ans = any isDivisorOf100 [a .. b]

  putStrLn $ yesNo ans

-- input functions
getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions
isDivisorOf100 :: Int -> Bool
isDivisorOf100 x = 100 `mod` x == 0

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

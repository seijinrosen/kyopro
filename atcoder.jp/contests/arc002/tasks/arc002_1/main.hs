isLeapYear :: Int -> Bool
isLeapYear n
  | n `mod` 400 == 0 = True
  | n `mod` 100 == 0 = False
  | n `mod` 4 == 0 = True
  | otherwise = False

yesNo :: Bool -> String
yesNo False = "NO"
yesNo True = "YES"

main :: IO ()
main = readLn >>= putStrLn . yesNo . isLeapYear

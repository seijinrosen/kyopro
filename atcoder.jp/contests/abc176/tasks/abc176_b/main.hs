import Data.Char (digitToInt)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

main :: IO ()
main = do
  n <- getLine

  let ans = sum (map digitToInt n) `mod` 9 == 0
  putStrLn $ yesNo ans

main :: IO ()
main = do
  n <- readLn
  putStrLn . yesNo . solve $ n

solve :: Int -> Bool
solve n
  | n `mod` 400 == 0 = True
  | n `mod` 100 == 0 = False
  | n `mod` 4 == 0 = True
  | otherwise = False

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

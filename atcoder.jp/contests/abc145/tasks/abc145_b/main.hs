yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

main :: IO ()
main = do
  n <- readLn
  s <- getLine

  let m = n `div` 2
      ans = take m s == drop m s

  putStrLn $ yesNo ans

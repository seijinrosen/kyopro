yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

solve :: String -> Bool
solve [] = False
solve [_] = False
solve [x, y] = [x, y] == "hi"
solve (x : y : xs) = [x, y] == "hi" && solve xs

main :: IO ()
main = do
  getLine >>= putStrLn . yesNo . solve

import Data.Char (isUpper)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

cond2 :: String -> Bool
cond2 s = case reads s of
  [(n, _)] -> 100000 <= n && n <= 999999
  _ -> False

solve :: String -> Bool
solve s = case length s of
  8 -> isUpper (head s) && cond2 (tail (init s)) && isUpper (last s)
  _ -> False

main :: IO ()
main = do
  getLine >>= putStrLn . yesNo . solve

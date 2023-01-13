import Data.List (isInfixOf)

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

main :: IO ()
main = interact $ yesNo . isInfixOf "AC"

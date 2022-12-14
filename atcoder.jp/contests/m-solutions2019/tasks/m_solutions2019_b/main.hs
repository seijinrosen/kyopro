import Util (count)

yesNo :: Bool -> String
yesNo False = "NO"
yesNo True = "YES"

main :: IO ()
main = do
  interact $ yesNo . (<= 7) . count (== 'x')

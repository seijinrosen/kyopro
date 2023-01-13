import Data.Bool (bool)
import Data.List (isPrefixOf)

main :: IO ()
main = do
  interact $ bool "No" "Yes" . isPrefixOf "YAKI"

import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

solve :: String -> Int
solve "Sunday" = 0
solve "Saturday" = 0
solve day = (5 -) . fromMaybe 0 . (`elemIndex` ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]) $ day

main :: IO ()
main = getLine >>= print . solve

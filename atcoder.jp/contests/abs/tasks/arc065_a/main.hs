import Data.List (stripPrefix)

candidates :: [String]
candidates = ["dream", "dreamer", "erase", "eraser"]

reversedCandidates :: [String]
reversedCandidates = map reverse candidates

main :: IO ()
main = do
  s <- getLine

  let ans = solve $ reverse s

  putStrLn . yesNo $ ans

solve :: String -> Bool
solve "" = True
solve s = maybe False solve (stripPrefixFromList reversedCandidates s)

stripPrefixFromList :: [String] -> String -> Maybe String
stripPrefixFromList [] _ = Nothing
stripPrefixFromList (prefix : prefixes) s = case stripPrefix prefix s of
  Just x -> Just x
  Nothing -> stripPrefixFromList prefixes s

yesNo :: Bool -> String
yesNo False = "NO"
yesNo True = "YES"

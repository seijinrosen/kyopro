import Data.List (find, isPrefixOf, stripPrefix)

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
solve s = case prefix of
  Nothing -> False
  Just p -> maybe False solve (stripPrefix p s)
  where
    prefix = findPrefix s

findPrefix :: String -> Maybe String
findPrefix s = find (`isPrefixOf` s) reversedCandidates

yesNo :: Bool -> String
yesNo False = "NO"
yesNo True = "YES"

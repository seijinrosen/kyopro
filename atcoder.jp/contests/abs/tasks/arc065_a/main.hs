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
solve s = case findPrefix s reversedCandidates of
  Nothing -> False
  Just prefix -> maybe False solve (stripPrefix prefix s)

findPrefix :: String -> [String] -> Maybe String
findPrefix s = find (`isPrefixOf` s)

yesNo :: Bool -> String
yesNo False = "NO"
yesNo True = "YES"

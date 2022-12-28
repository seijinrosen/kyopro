main :: IO ()
main = getLine >>= putStrLn . yesNo . isPalindrome . rstrip '0'

isPalindrome :: Eq a => [a] -> Bool
isPalindrome s = reverse s == s

rstrip :: Eq a => a -> [a] -> [a]
rstrip c = reverse . dropWhile (== c) . reverse

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

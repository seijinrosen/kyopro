import qualified Data.Text as T

countText :: String -> String -> Int
countText s = T.count (T.pack s) . T.pack

main :: IO ()
main = do
  s <- getLine

  let ans = countText "ZONe" s
  print ans

import Util (count)

main :: IO ()
main = do
  n <- getLine
  print $ count (== '2') n

import Util (count)

main :: IO ()
main = do
  s <- getLine
  print $ count (== '1') s

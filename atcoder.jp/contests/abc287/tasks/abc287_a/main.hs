import Control.Monad (replicateM)
import Util (count)

main :: IO ()
main = do
  n <- readLn
  s <- replicateM n getLine

  let ans = n `div` 2 < count (== "For") s

  putStrLn $ if ans then "Yes" else "No"

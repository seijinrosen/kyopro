import Data.Function ((&))
import Data.List (elemIndex)
import Data.Maybe (fromMaybe)

main :: IO ()
main = do
  s <- getLine
  let ans = solve s
  putStrLn ans

solve :: String -> String
solve s = show (n `div` g) ++ "/" ++ show (d `div` g)
  where
    i = elemIndex '/' s & fromMaybe 0
    p = splitAt i s
    n = p & fst & read
    d = p & snd & tail & read
    g = gcd n d

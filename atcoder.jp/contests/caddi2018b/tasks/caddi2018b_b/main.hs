import Control.Monad (replicateM)
import Util (count)

main :: IO ()
main = do
  [n, h, w] <- map read . words <$> getLine
  ab <- replicateM n $ (\[a, b] -> (a, b)) . map read . words <$> getLine

  print $ count (\(a, b) -> h <= a && w <= b) ab

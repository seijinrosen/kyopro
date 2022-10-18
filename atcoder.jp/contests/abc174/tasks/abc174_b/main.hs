import Control.Monad (replicateM)
import Util (count)

main :: IO ()
main = do
  [n, d] <- map read . words <$> getLine
  xy <- replicateM n $ (\[x, y] -> (x, y)) . map read . words <$> getLine

  let ans = count (\(x, y) -> x ^ 2 + y ^ 2 <= d ^ 2) xy
  print ans

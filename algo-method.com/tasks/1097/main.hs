import Control.Monad (replicateM)
import qualified Data.Map as Map
import Data.Maybe (fromMaybe)

main :: IO ()
main = do
  [n, m] <- map read . words <$> getLine
  fc <- replicateM n $ words <$> getLine
  xs <- words <$> getLine

  let menu = Map.fromList [(f, read c) | [f, c] <- fc]
      ans = sum [fromMaybe 0 $ Map.lookup x menu | x <- xs]

  print ans

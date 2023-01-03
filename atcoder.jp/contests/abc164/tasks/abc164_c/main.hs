import Control.Monad (replicateM)
import qualified Data.Set as Set

main :: IO ()
main = do
  n <- readLn
  s <- replicateM n getLine

  let st = Set.fromList s
      ans = Set.size st

  print ans

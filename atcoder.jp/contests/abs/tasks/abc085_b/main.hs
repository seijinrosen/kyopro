import Control.Monad (replicateM)
import Data.Set (fromList)

main :: IO ()
main = do
  n <- getInt
  d <- getVerticalIntList n

  let ans = length . fromList $ d

  print ans

-- input functions

getInt :: IO Int
getInt = readLn

getVerticalIntList :: Int -> IO [Int]
getVerticalIntList n = replicateM n getInt

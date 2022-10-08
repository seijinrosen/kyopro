import Control.Monad (replicateM)
import Data.Vector (fromList, (!))

main :: IO ()
main = do
  [n, q] <- getIntList
  a <- getIntList
  lr <- getIntPairList q

  let acc = fromList $ 0 : accumulate a
      ans = [acc ! r - acc ! (l -1) | (l, r) <- lr]

  printVertically ans

-- input functions

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

toPair :: [Int] -> (Int, Int)
toPair [p, q] = (p, q)
toPair _ = (0, 0)

getIntPair :: IO (Int, Int)
getIntPair = toPair . map read . words <$> getLine

getIntPairList :: Int -> IO [(Int, Int)]
getIntPairList n = replicateM n getIntPair

-- print functions

printVertically :: (Foldable t, Show a) => t a -> IO ()
printVertically = mapM_ print

-- functions

accumulate :: [Int] -> [Int]
accumulate [] = []
accumulate [x] = [x]
accumulate (x : y : xs) = x : accumulate (x + y : xs)

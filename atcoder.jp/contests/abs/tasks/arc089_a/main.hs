import Control.Monad (replicateM)

main :: IO ()
main = do
  n <- getInt
  txy <- getIntListList n

  let ans = all ok . pairwise $ [0, 0, 0] : txy

  putStrLn . yesNo $ ans

ok :: ([Int], [Int]) -> Bool
ok ([t, x, y], [t', x', y']) = 0 <= time && even time
  where
    dist = abs (x' - x) + abs (y' - y)
    time = t' - t - dist
ok _ = False

-- input functions

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

getIntListList :: Int -> IO [[Int]]
getIntListList n = replicateM n getIntList

-- functions

pairwise :: [b] -> [(b, b)]
pairwise iterable = zip iterable $ tail iterable

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

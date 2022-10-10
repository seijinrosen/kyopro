import Control.Monad (replicateM)

main :: IO ()
main = do
  info <- getIntTupleList 30

  let ans = solve info

  putStrLn $ show (fst ans) ++ " " ++ show (snd ans)

solve :: [(Int, Int, Int, Int)] -> (Int, Int)
solve info = toHourAndMinute . sum $ [subtractBreakTime $ toMinute eh em - toMinute sh sm | (sh, sm, eh, em) <- info]

toMinute :: Int -> Int -> Int
toMinute h m = 60 * h + m

subtractBreakTime :: Int -> Int
subtractBreakTime m
  | m <= 360 = m
  | m <= 480 = m - 45
  | otherwise = m - 60

toHourAndMinute :: Int -> (Int, Int)
toHourAndMinute m = (m `div` 60, m `mod` 60)

-- input functions

toTuple :: [Int] -> (Int, Int, Int, Int)
toTuple [p, q, r, s] = (p, q, r, s)
toTuple _ = (0, 0, 0, 0)

getIntTuple :: IO (Int, Int, Int, Int)
getIntTuple = toTuple . map read . words <$> getLine

getIntTupleList :: Int -> IO [(Int, Int, Int, Int)]
getIntTupleList n = replicateM n getIntTuple

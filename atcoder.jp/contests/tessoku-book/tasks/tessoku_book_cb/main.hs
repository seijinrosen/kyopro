main :: IO ()
main = do
  n <- getInt
  as <- getIntList

  let ans = any (\comb -> sum comb == 1000) $ combinations as 3
  putStrLn $ yesNo ans

-- input functions

getInt :: IO Int
getInt = readLn

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

-- functions

-- https://wiki.haskell.jp/Old/sampou.org/Programming_玉手箱#組合せの生成
combinations :: [a] -> Int -> [[a]]
combinations _ 0 = [[]]
combinations [] _ = []
combinations (x : xs) n = map (x :) (combinations xs (n - 1)) ++ combinations xs n

yesNo :: Bool -> String
yesNo False = "No"
yesNo True = "Yes"

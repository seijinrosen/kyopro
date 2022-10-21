main :: IO ()
main = do
  n <- readLn :: IO Int
  d <- map read . words <$> getLine

  let ans = sum [x * y | [x, y] <- combinations d 2]
  print ans

-- https://wiki.haskell.jp/Old/sampou.org/Programming_玉手箱#組合せの生成
combinations :: [a] -> Int -> [[a]]
combinations _ 0 = [[]]
combinations [] _ = []
combinations (x : xs) n = map (x :) (combinations xs (n - 1)) ++ combinations xs n

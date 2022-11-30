-- https://wiki.haskell.jp/Old/sampou.org/Programming_玉手箱#組合せの生成
combinations :: [a] -> Int -> [[a]]
combinations _ 0 = [[]]
combinations [] _ = []
combinations (x : xs) n = map (x :) (combinations xs (n - 1)) ++ combinations xs n

main :: IO ()
main = do
  abcd <- map read . words <$> getLine

  let ans = sum abcd `elem` [sum comb * 2 | r <- [1, 2, 3], comb <- combinations abcd r]
  putStrLn $ if ans then "Yes" else "No"

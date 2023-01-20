import Util (count)

main :: IO ()
main = do
  n <- readLn
  p <- map read . words <$> getLine

  let cnt = count (== True) $ zipWith (/=) [1 .. n] p
      ans = cnt == 0 || cnt == 2

  putStrLn $ if ans then "YES" else "NO"

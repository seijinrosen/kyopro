main :: IO ()
main = do
  [x, y] <- map read . words <$> getLine

  let ans = 4 * x - y `elem` map (2 *) [0 .. x]

  putStrLn $ if ans then "Yes" else "No"

import Util (count)

step2 :: [a] -> [a]
step2 [] = []
step2 [x] = [x]
step2 (x : y : xs) = x : step2 xs

main :: IO ()
main = do
  n <- readLn :: IO Int
  a <- map read . words <$> getLine

  let ans = count odd $ step2 a
  print ans

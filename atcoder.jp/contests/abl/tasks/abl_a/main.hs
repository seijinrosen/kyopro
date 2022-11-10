repeatStr :: Int -> [a] -> [a]
repeatStr n = concat . replicate n

main :: IO ()
main = do
  k <- readLn

  let ans = repeatStr k "ACL"
  putStrLn ans

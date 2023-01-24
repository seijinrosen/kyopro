relu :: (Ord p, Num p) => p -> p
relu x
  | x >= 0 = x
  | otherwise = 0

main :: IO ()
main = readLn >>= print . relu

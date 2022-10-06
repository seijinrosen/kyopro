import Data.Bits (Bits (shiftL, (.&.)))

main :: IO ()
main = do
  [n, x] <- getIntList

  let ans = length [i | i <- [0 .. n - 1], 0 < 1 `shiftL` i .&. x]

  print ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

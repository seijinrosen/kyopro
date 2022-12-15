import Util (count)

isProductDay :: (Int, Int) -> Bool
isProductDay (m, d) = (d1 >= 2) && (d10 >= 2) && (d1 * d10 == m)
  where
    (d10, d1) = d `divMod` 10

solve :: Int -> Int -> Int
solve m d = count isProductDay [(m', d') | m' <- [1 .. m], d' <- [1 .. d]]

main :: IO ()
main = do
  [m, d] <- map read . words <$> getLine
  print $ solve m d

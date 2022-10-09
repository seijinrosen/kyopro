main :: IO ()
main = do
  [h, w, p, q] <- getIntList

  let ans =
        if even (p + q)
          then "Black"
          else "White"

  putStrLn ans

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

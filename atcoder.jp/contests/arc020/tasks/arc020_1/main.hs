main :: IO ()
main = do
  [a, b] <- map read . words <$> getLine

  let ans = case abs a `compare` abs b of
        LT -> "Ant"
        EQ -> "Draw"
        GT -> "Bug"

  putStrLn ans

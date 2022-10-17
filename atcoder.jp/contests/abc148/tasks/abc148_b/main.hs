import Control.Monad (join)

main :: IO ()
main = do
  n <- readLn :: IO Int
  [s, t] <- words <$> getLine

  let ans = join [[s, t] | (s, t) <- zip s t]

  putStrLn ans

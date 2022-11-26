import Control.Monad (replicateM)

main :: IO ()
main = do
  n <- readLn
  st <- replicateM n $ do
    [s, t] <- words <$> getLine
    return (s, read t)
  x <- getLine

  let ans = sum . map snd . tail $ dropWhile ((/= x) . fst) st
  print ans

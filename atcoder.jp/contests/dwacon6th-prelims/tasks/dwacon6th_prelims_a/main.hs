import Control.Monad (replicateM)

main :: IO ()
main = do
  n <- readLn
  st <- replicateM n $ (\[p, q] -> (p, read q)) . words <$> getLine
  x <- getLine

  let ans = sum . map snd . tail $ dropWhile (\(s, t) -> s /= x) st
  print ans

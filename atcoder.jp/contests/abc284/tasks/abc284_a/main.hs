import Control.Monad (replicateM)

main :: IO ()
main = do
  n <- readLn
  s <- replicateM n getLine

  let ans = reverse s

  mapM_ putStrLn ans

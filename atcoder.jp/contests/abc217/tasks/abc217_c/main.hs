import Data.List (sort)

showIntList :: [Int] -> String
showIntList = unwords . map show

getIntList :: IO [Int]
getIntList = map read . words <$> getLine

main :: IO ()
main = do
  n <- readLn :: IO Int
  p <- getIntList

  let ans = map snd . sort $ zip p [1 ..]
  putStrLn $ showIntList ans

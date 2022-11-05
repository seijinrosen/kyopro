import Data.List (findIndices)

findIndexR :: (a -> Bool) -> [a] -> Int
findIndexR p xs
  | null indices = -1
  | otherwise = last indices
  where
    indices = findIndices p xs

main :: IO ()
main = do
  s <- getLine

  let i = findIndexR (== 'a') s
      ans = if i == -1 then -1 else i + 1

  print ans

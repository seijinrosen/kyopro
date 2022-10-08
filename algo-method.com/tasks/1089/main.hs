main :: IO ()
main = do
  n <- getInt

  let ans = map solve [1 .. n]

  putStrLnVertically ans

solve :: Int -> String
solve n = if ret == "" then show n else ret
  where
    fizz = if n `mod` 4 == 0 then "Fizz" else ""
    buzz = if n `mod` 6 == 0 then "Buzz" else ""
    ret = fizz ++ buzz

-- input functions

getInt :: IO Int
getInt = readLn

-- print functions

putStrLnVertically :: [String] -> IO ()
putStrLnVertically = mapM_ putStrLn

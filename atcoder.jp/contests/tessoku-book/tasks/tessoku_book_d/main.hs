import Data.Char (intToDigit)

main :: IO ()
main = do
  n <- getInt

  let ans = zfill 10 . int2bin $ n

  putStrLn ans

-- input functions

getInt :: IO Int
getInt = readLn

-- functions

int2bin :: Int -> String
int2bin 0 = "0"
int2bin 1 = "1"
int2bin num = int2bin (num `div` 2) ++ [intToDigit $ num `mod` 2]

zfill :: Int -> String -> String
zfill width s
  | diff <= 0 = s
  | otherwise = replicate diff '0' ++ s
  where
    diff = width - length s

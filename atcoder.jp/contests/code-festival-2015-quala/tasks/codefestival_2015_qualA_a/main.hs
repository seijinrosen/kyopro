main :: IO ()
main = getLine >>= putStrLn . (++ "5") . init

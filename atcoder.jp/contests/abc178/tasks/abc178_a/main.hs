main :: IO ()
main = readLn >>= print . (1 -)

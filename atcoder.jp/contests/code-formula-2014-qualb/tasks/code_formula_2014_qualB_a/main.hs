main :: IO ()
main = readLn >>= print . (7 -)

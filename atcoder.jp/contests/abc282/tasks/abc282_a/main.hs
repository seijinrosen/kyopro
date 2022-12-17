main :: IO ()
main = do
  interact $ (`take` ['A' .. 'Z']) . read

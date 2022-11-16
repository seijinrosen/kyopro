import Data.Char (toUpper)

main :: IO ()
main = do
  s <- head <$> getLine
  t <- head <$> getLine

  let ans = if s == 'Y' then toUpper t else t
  putStrLn [ans]

import qualified Data.Map as Map
import Data.Maybe (fromMaybe)

main :: IO ()
main = do
  s <- getLine

  let d = Map.fromList [('6', '9'), ('9', '6')]
      ans = map (translate d) $ reverse s

  putStrLn ans

translate :: Ord k => Map.Map k k -> k -> k
translate mp x = fromMaybe x $ Map.lookup x mp

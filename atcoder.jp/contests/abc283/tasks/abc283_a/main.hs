main = interact $ show . (\[a, b] -> a ^ b) . map read . words

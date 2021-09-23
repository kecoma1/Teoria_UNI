module Main where

removeNonUpperCase :: [Char] -> [Char]
removeNonUpperCase st = [ c | c <- st, c 'elem' ['A'..'Z']]

main :: IO ()
main = 
    do
        print var2;
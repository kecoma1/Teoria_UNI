module Ejemplos where
    removeNonUpperCase :: [Char] -> [Char]
    removeNonUpperCase st = [ c | c <- st, c `elem` ['A'..'Z']]

    addThree :: Int -> Int -> Int -> Int
    addThree x y z = x + y + z

    cabeza :: [a] -> a
    cabeza (x:xs) = x

    lucky :: Int -> [Char]
    lucky 5 = "Graaandeee"
    lucky x = "La proxima habra mas suerte chavaal"

    factorial :: Integer -> Integer
    factorial 0 = 1
    factorial x = x * factorial (x-1)

    addVectors :: Num a => (a, a) -> (a, a) -> a
    addVectors (x1, y1) (x2, y2) = (x1 + x2) * (y1 + y2)

    first :: Show a => (a, a, a) -> a
    first (x, _, _) = x
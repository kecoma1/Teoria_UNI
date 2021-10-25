module Ejercicios2 where

sumar :: Integer -> Integer -> Integer
sumar x y = x + y

sumar' :: Integer -> Integer -> Integer
sumar' x = (+) x

sumar'' :: Integer -> Integer -> Integer
sumar'' = (+)

prodEscalar :: Num a => (a, a) -> (a, a) -> a
prodEscalar (x1, y1) (x2, y2) = x1*x2 + y1*y2

prodEscalar' :: Num a => (a, a) -> (a, a) -> a
prodEscalar' (x, y) = prodEscalar (x, y)

prodEscalar'' :: Num a => (a, a) -> (a, a) -> a
prodEscalar'' = prodEscalar

prod :: Integer -> Integer -> Integer -> Integer -> Integer
prod x y z t = x*y*z*t

prod' :: Integer -> Integer -> Integer -> Integer -> Integer
prod' x y z = prod x y z

prod'' :: Integer -> Integer -> Integer -> Integer -> Integer
prod'' x y = f
    where f = prod' x y

prod''' :: Integer -> Integer -> Integer -> Integer -> Integer
prod''' x = case x of
    0 -> prod'' 1
    x -> prod'' x

prod'''' :: Integer -> Integer -> Integer -> Integer -> Integer
prod'''' = prod'''

[ ((sumar x y == sumar' x y) &&)  == sumar'' x y  | x <- [1..10], y <- x*2 ]
module Boberías where

type Funcion = Integer -> Integer

curryes :: ((a, b) -> c) -> a -> b -> c
curryes f x y = f (x, y)

uncurryes :: (a -> b -> c) -> ((a, b) -> c)
uncurryes f (x, y) = f x y

fwhere :: Integer -> Integer -> Integer
fwhere x y = z + x + y 
    where z = 3

f2_1 :: Integer -> Integer
f2_1 x 
        | x > 1000 = x+1
        | x > 100 = 2*x+1
        | otherwise = 3*x+1

fcase :: [Integer] -> Integer
fcase y = case y of
    (x:1:xs) -> 1
    (2:xs) -> 2
    (3:xs) -> 3
    (x:5:6:xs) -> 56
    _ -> 0

fwhere2 :: Integer -> Integer
fwhere2 x = x*y*z+t+b
            where y = 2
                  z = 3
                  t = 4
                  b = if x < 10 
                      then 12
                      else 1

flet :: Integer -> Integer
flet x = let y = 2
             z = 3
             t = 4
             b = if x < 10
                 then 12
                 else 1
             in x*y*z+t+b

fwhere3 :: Integer -> Integer
fwhere3 x = x + g y * c
            where 
                g :: Integer -> Integer
                g t = 2*t
                y = 10
                c = 100

flet2 :: Integer -> Integer
flet2 x = let g :: Integer -> Integer
              g t = 2*t
              y = 10
              c = 100
            in x + g y * c

fwhere4 :: Integer -> Integer
fwhere4 x = if x < 10 then x
            else g x * y
            where
                g :: Integer -> Integer
                g z = z*4
                y = 10

flet3 :: Integer -> Integer
flet3 x = let g :: Integer -> Integer
              g z = z*4
              y = 10
          in if x < 10 then x
             else g x * y  

fwhere5 :: Integer -> Integer
fwhere5 x = x*z + y*x
    where z = 3
          y = 2

flet4 :: Integer -> Integer
flet4 x = let z = 3
              y = 2
          in x*z + y*x

fguard :: Integer -> Integer
fguard x 
        | x > 100 = x-z
        | x > 10 = x-y
        | otherwise = x
        where z = 10
              y = 1

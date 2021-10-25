doublesmallnumber :: Integer -> Integer
doublesmallnumber x =   if x <= 100 
                        then x*2 
                        else x

doublesmallnumber2 :: Integer -> Integer
doublesmallnumber2 x
                        | x <= 100 = x*2
                        | otherwise = x

cadena :: [Char]
cadena = "cadena"

longitud :: [a] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

cadenamas7 = longitud cadena + 7

entero :: Integer
entero = 1

polim :: Num a => a
polim = 1

tupla1 :: Num b => (Integer, b)
tupla1 = (entero, polim)

lista1 :: [Integer]
lista1 = [entero, polim]

suma1 :: Integer -> Integer -> Integer
suma1 x y = x + y

suma2 :: Num a => a -> a -> a
suma2 x y = x+y


data Point = Point Float Float deriving (Show)
addCords :: Point -> Float
addCords (Point x y) = x + y

data Shape = Circle Point Float | Rectangle Point Point deriving (Show)
circle1 :: Shape
circle1 = Circle (Point 1 2) 4

surface :: Shape -> Float
surface (Circle _ r) = pi*r^2
surface (Rectangle (Point a b) (Point c d)) = abs(a - b) * abs (b - c)

type ListaEnteros = [Integer]
lista2 :: ListaEnteros
lista2 = [1..5]

data Numero = Entero Integer | Decimal Float deriving (Show)

ent1 :: Numero
ent1 = Entero 1

ent2 :: Numero
ent2 = Entero 2

dec1 :: Numero
dec1 = Decimal 2.5

type FuncionEntreEnteros = Numero -> Numero -> Numero

sumaEntreEnteros :: FuncionEntreEnteros
sumaEntreEnteros (Entero x) (Entero y) = Entero (x + y)

psum :: Numero -> Numero
psum x = sumaEntreEnteros (Entero 2) x

sumar :: Integer -> Integer -> Integer
sumar x y = x + y

sumar' :: Integer -> Integer -> Integer
sumar' x = (+) x

sumar'' :: Integer -> Integer -> Integer
sumar'' = (+)

data Vector = Vector Double Double deriving (Show)

prodEscalar :: Vector -> Vector -> Double
prodEscalar (Vector x1 y1) (Vector x2 y2) = x1*x2 + y1*y2

comprobarSumar:: (Integer,Integer)->Bool
comprobarSumar (x1,x2) = sumar x1 x2 == sumar' x1 x2
                         && sumar' x1 x2 == sumar'' x1 x2
comp :: [((Integer, Integer), Bool)]
comp=[((x,y),comprobarSumar (x,y)) | x<-[1..10], y<-[1..x], mod x y == 0]


module Ej4 where

data Cuadrado = Cuad {bordeX::Int, bordeY::Int, ancho::Int,color::Char} deriving (Read, Show)
type Cuadrados=[Cuadrado]

-- Suponemos todas las cadenas de la misma longitud (maximo)
type Mosaico = [String]

maximo=10

mosaicoInicial :: Mosaico
mosaicoInicial =  replicate maximo $ replicate maximo '.'

cuad1, cuad2, cuad3 :: Cuadrado
cuad1=Cuad 2 3 2 'a'
cuad2=Cuad 1 5 2 'b'
cuad3=Cuad 4 2 3 'c'

cuads :: [Cuadrado]
cuads=[cuad1,cuad2,cuad3]

incluirCuadrados :: Mosaico -> [Cuadrado] -> Mosaico
incluirCuadrados=foldl incluirCuadrado

-- Superpone el cuadrado en las posiciones del mosaico
incluirCuadrado :: Mosaico -> Cuadrado -> Mosaico
incluirCuadrado mosaico cuadrado = map fila [1..maximo]
    where fila n = map (letra n) [1..maximo]
    (letra n) m = if (dentroCuadrado n m cuadrado) then
    color cuadrado else mosaico !! (n-1) !! (m-1)

girarHorizontal :: Mosaico->Mosaico
girarHorizontal = <???> -- usando función “reverse”

girarVertical :: Mosaico->Mosaico
girarVertical = <???> -- usando función “reverse”

dibujarMosaico :: Mosaico -> IO ()
dibujarMosaico = putStrLn . unlines

mostrarSeparador :: IO ()
mostrarSeparador = <???> -- usando función “replicate”

main4 :: IO ()
main4 = do  dibujarMosaico mosaicoInicial
            let mosaico1=incluirCuadrado mosaicoInicial cuad1
            mostrarSeparador
            dibujarMosaico mosaico1
            mostrarSeparador
            dibujarMosaico $ incluirCuadrados mosaicoInicial cuads
            mostrarSeparador
            dibujarMosaico $ girarHorizontal mosaico1
            mostrarSeparador
            dibujarMosaico $ girarVe
            
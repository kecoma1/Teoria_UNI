data Cuadrado = Cuad {bordeX::Int, bordeY::Int, ancho::Int,color::Char} deriving (Read, Show)
type Cuadrados=[Cuadrado]

-- Suponemos todas las cadenas de la misma longitud (maximo)
type Mosaico = [String]

maximo=10

mosaicoInicial :: Mosaico
mosaicoInicial = replicate maximo $ replicate maximo '.'

dibujarMosaico :: Mosaico -> IO ()
dibujarMosaico = putStrLn . unlines

-- Superpone el cuadrado en las posiciones del mosaico
incluirCuadrado :: Mosaico -> Cuadrado -> Mosaico
incluirCuadrado mosaico cuadrado = map fila [1..maximo]
    where fila n = map (letra n) [1..maximo]
          (letra n) m = if (dentroCuadrado n m cuadrado) then color cuadrado else mosaico !! (n-1) !! (m-1)

dentroCuadrado :: Int -> Int -> Cuadrado -> Bool
dentroCuadrado x y c = if x < 
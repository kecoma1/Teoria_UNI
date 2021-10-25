module Ejercicios where

data Complejo = Comp Double Double | (:::) Double Double deriving (Show)

sumarComplejo :: Complejo -> Complejo -> Complejo
sumarComplejo (Comp x1 y1) (Comp x2 y2) = Comp (x1+x2) (y1+y2)
sumarComplejo (Comp x1 y1) (x2 ::: y2) = Comp (x1+x2) (y1+y2)
sumarComplejo (x1 ::: y1) (Comp x2 y2) = Comp (x1+x2) (y1+y2)
sumarComplejo (x1 ::: y1) (x2 ::: y2) = Comp (x1+x2) (y1+y2)

multiplicarComplejo :: Complejo -> Complejo -> Complejo
multiplicarComplejo (Comp a b) (Comp c d) = Comp (a*c - b*d) (a*d + b*c)
multiplicarComplejo (Comp a b) (c ::: d) = Comp (a*c - b*d) (a*d + b*c)
multiplicarComplejo (a ::: b) (Comp c d) = Comp (a*c - b*d) (a*d + b*c)
multiplicarComplejo (a ::: b) (c ::: d) = Comp (a*c - b*d) (a*d + b*c)
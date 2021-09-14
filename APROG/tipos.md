# Tipos de datos Hashkell
Para consultar el tipo de un dato usamos:
```hs
:t []
:type []
```

En hashkell tenemos tipos _básicos_ como _Bool_, _Char_, _Int_, _Integer_, _Word_, _Float_, _Double_...

También tenemos tipos _compuestos_ como:
* **Lista**: Las listas estan compuestas de elementos del __mismo tipo__.
    ```hs
    :type []
    [] :: [a]
    ```
*  **Tuplas**: Tienen elementos de __diferente tipo__ o __el mismo__. Las tuplas solo pueden tener 0, 2 o más elementos, __nunca 1__.
    ```hs
    (T1, T2, …, TN) (N≥=2 o N=0)
    ```

* **Funciones**: Donde el último elemento en la sucesión de flechas es el tipo del elemento que se devuelve, los anteriores son argumentos. Por ejemplo, el operando suma es una función que acepta __2__ argumentos que pertenezcan al tipo _Num_ (todos deben ser iguales), y devuelve un elemento del tipo _Num_.
    ```hs
    T1->T2->…->TN->T (N ≥ 1)

    :type (+)
    (+) :: Num a => a -> a -> a
    ```

En hashkell tenemos __identificadores__ y a estos se les puede asignar tipos.
```hs
x :: Char -- asignación tipo
x='a' -- declaración valor
```
Hashkell también _infiere_ los tipos en tiempo de compilación.


-- LOOPS IN HASKELL
-- Instead of using functions to do loops, Haskell uses recursion.

-- FOR LOOP
{-
This is how a for-loop would look is most other languages, like C#.
int forLoop(int maxLoopNr, int value)
{
    for (int = 0; loopNr < maxLoopNr; loopNr++)
    {
        value += 3;
    }

    return value;
}
-}

-- Input is 3 Ints and return is an Int
-- VARIANT: loopNr == maxLoopNr
forLoop :: Int -> Int -> Int -> Int
forLoop loopNr maxLoopNr value =
    if loopNr < maxLoopNr
        then forLoop (loopNr + 1) maxLoopNr (3 + loopNr)
        else value

-- FOREACH LOOP
{-
Counts the number of elements in a string.
int forEach(string stringData)
{
    int num = 0;
    foreach (char c in stringData)
    {
        num++;
    }
    return num;
}
-}

-- VARIANT: length string == 0
forEach :: String -> Int
forEach [] = 0
forEach (char:stringData) = 1 + (forEach stringData)

-- WHILE LOOP
{-
int whileLoop(int a)
{
    while (a % 7 != 0)
    {
        a++;
    }

    return a;
}
-}

-- VARIANT: a + 1 == mod 7
whileLoop :: Int -> Int
whileLoop a =
    if (a `mod` 7) != 0
        then whileLoop (a + 1)
        else a
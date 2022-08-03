
#!/usr/bin/env python3
# Following https://www.woolseyworkshop.com/2020/06/25/documenting-python-programs-with-doxygen/ to write doxygen formated documentation or VSC plugins auto suggestion.

def main():
    dimsQ = "Enter the number of dimensions of the matrix (number of elements in each vector): "
    nrVectorsQ = "Enter the number of vectors: "
    dims = getPositiveInt(dimsQ)
    nrVectors = getPositiveInt(nrVectorsQ)
    matrix = []
    
    # For each vector, ask the user what the data is
    for i in range(nrVectors):
        matrix.append(getAVector(dims))
    prettyPrintMatrix(matrix)
        
def prettyPrintMatrix(matrix):
    """Takes a list of lists which is intended to be a matrix as arguments and prints it as both a multi-line matrix and a singleline matrix. The singleline is intended to be easy to copy to a different program, such as Wolfram Alpha

    Args:
        matrix ([[number]]): A representation of a matrix with the inner lists being vectors.
    """
    multiLineString = multiLinePrintMatrix(matrix)
    singleLineString = singleLinePrintMatrix(multiLineString)
    print("Multi line matrix:")
    print(multiLineString)
    print("Single line matrix")
    print(singleLineString)
    
def multiLinePrintMatrix(matrix):
    """Converts the matrix to a printfriendly multi-line matrix with '{' at the start of each vector and ',' to seperate each entry.

    Args:
        matrix ([[number]]): A representation of a matrix with the inner lists being vectors.
        
    Returns:
        string: A multi-line matrix with '{' at the start of each vector and ',' to seperate each entry.
    """
    def vectorToString(vector):
        """Reads a list of numbers and returns a string formated with '{}' brackets at the beginning and end. And each entry seperated by ','.
        It's a function within a function to show off using it as such, rather than it being particularly useful.

        Args:
            vector ([number]): A list with numbers representing a vector.

        Returns:
            string: A single-line string formated with '{}' brackets at the beginning and end. And each entry seperated by ','.
        """
        returnString = "{"
        for entry in vector:
            returnString += str(entry)
            if entry != vector[-1]: returnString += ","
        returnString += "}"
        return returnString
    returnString = "{"
    for vector in matrix:
        returnString += vectorToString(vector)
        if vector != matrix[-1]: returnString += ",\n"
    returnString += "}"
    return returnString
    
def singleLinePrintMatrix(matrixPrint):
    """Returns a single-line version of a multi-line string represenation of a matrix, by stripping the newline characters.

    Args:
        matrixPrint (string): A multi-line matrix string represenation of a matrix.

    Returns:
        string: A single-line string representation of a matrix.
    """
    return matrixPrint.replace('\n', '')
    
def getAVector(vectorSize):
    """Gets each entry of the vector from the user. Each entry is of type float.

    Args:
        vectorSize (int): The number of elements in the vector.

    Returns:
        [float]: A list representing a vector.
    """
    returnVector = []
    vectorQ = "Enter data for x_"
    for i in range(vectorSize):
        # The allowed number type is float
        returnVector.append(getNumberOfTypeFromUser(vectorQ + str(i) + ": ", float))
    return returnVector
    
def getPositiveInt(explainInput):
    """Repeatedly asks the user for a positive integer until one is provided. This integer is then returned.

    Args:
        explainInput (string): The explaination of the integer will be used for.

    Returns:
        int: A positive integer.
    """
    validAnswer = False
    returnInt = -1
    while not validAnswer:
        # The allowed number type is int
        returnInt = getNumberOfTypeFromUser(explainInput, int)
        if returnInt > 0: validAnswer = True
        if returnInt <= 0: print("Number needs to be positive, try again.")
    return returnInt
    
def getNumberOfTypeFromUser(explainInput, typeConversionFunction):
    """Gets a number from the user of type set by typeConversionFunction function which converts the string to the desired number type. It will repeatedly ask the users for a number until it gets an answer which does not produce an exception when trying to convert the string.

    Args:
        explainInput (string): The explaination of what the number will be used for.
        typeConversionFunction (function): A function which converts a string to the desired number type. Eg. 'int' or 'float'.

    Returns:
        number: String converted to the type set by typeConversionFunction.
    """
    validAnswer = False
    returnNumber = -1
    while not validAnswer:
        try:
            returnNumber = typeConversionFunction(input(explainInput))
            validAnswer = True
        except:
            print("Invalid input, try again (only numbers allowed).")
    return returnNumber

##
# If this scripts is being executed as a program rather than a library, the statement evaulates to True
if __name__ == "__main__":
    main()
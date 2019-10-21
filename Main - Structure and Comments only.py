# My second Python application


# Variables (must be declared BEFORE using them)
# ---------

# Define variables for data (LastName and FirstName)
LastName = ""
FirstName = ""


# Methods (must be declared BEFORE using them)
# -------

def GetData():
    """ 
        Get data (First and Last names)

        :return: returns an error in data if appropriate
            - "" if no error
            - "LF" if LastName and FirstName are empty
            - "L" if only LastName is empty
            - "F" if only FirstName is empty
        :rtype: string
    """

    # Use global variables (defined at beginning of file)
    global LastName
    global FirstName

    # Ask for names if they are empty
    # TODO

    # Check if names are empty
    # TODO


def ShowResult(ErrorMessage):
    """ 
        Show data result
            - Welcome if all data is valid
            - Error message if not

        :param arg1: An error message if any
        :type arg1: string
    """

    # Check for an error message
    if (ErrorMessage == "LF"):
        # Missing both names
        # TODO
        pass
    elif (ErrorMessage == "L"):
        # Missing LastName
        # TODO
        pass
    elif (ErrorMessage == "F"):
        # Missing FirstName
        # TODO
        pass
    else:
        # Both names are not empty
        # Say welcome
        # TODO
        pass


# Application
# -----------

# Say Hello to user
print("Bonjour humain, veuillez vous identifier afin que je puisse interagir avec vous.")

# While LastName or FirstName are empty
while (LastName == "" or FirstName == ""):

    # Print a blank line
    print()

    # Ask for names if they are empty
    # and check if an error occurs
    DataError = GetData()

    # Show result 
    ShowResult(DataError)

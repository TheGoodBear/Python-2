# My first Python application

# Define variables for LastName and FirstName
LastName = ""
FirstName = ""

# Say Hello to user
print("Bonjour humain, veuillez vous identifier afin que je puisse interagir avec vous.")

# While LastName or FirstName are empty
while (LastName == "" or FirstName == ""):

    # Print a blank line
    print()

    # Ask for names if they are empty
    # and check if an error occurs
    DataError = GetNames()

    # Show result 
    ShowResult(DataError)


# Methods

def GetNames():
    """ 
        Get First and Last names

        :return: returns if an error is encoutered
            - "" if no error
            - "LF" if LastName and FirstName are empty
            - "L" if only LastName is empty
            - "F" if only FirstName is empty
        :rtype: string
    """

    # Use global variables (defined at file start)
    global LastName
    global FirstName

    # Ask for names if they are empty
    if (FirstName == ""):
        FirstName = input("Veuillez entrer votre prénom : ")
    if (LastName == ""):
        LastName = input("Veuillez entrer votre nom : ")

    # Check if names are empty
    if (LastName == "" and FirstName == ""):
        return "LF"
    elif (LastName == ""):
        return "L"
    elif (FirstName == ""):
        return "F"


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
        print("Le prénom et le nom entrés sont vides, veuillez recommencer.")
    elif (ErrorMessage == "L"):
        # Missing LastName
        print("Le nom entré est vide, veuillez compléter.")
    elif (ErrorMessage == "F"):
        # Missing FirstName
        print("Le prénom entré est vide, veuillez compléter.")
    else:
        # Both names are not empty
        # Say welcome
        print()
        print("Enchanté", FirstName, LastName, ", je te souhaite une belle journée.")

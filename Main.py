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
        # By using string concatenation (+)
        print("Enchanté " + FirstName + " " + LastName + ", je te souhaite une belle journée.")
        # By using print separator (,)
        print("Enchanté", FirstName, LastName, ", je te souhaite une belle journée.")
        # By using string placeholders (%)
        print(
            "Enchanté %s %s, je te souhaite une belle journée." 
            % (FirstName, LastName))
        # By using string formating ({} and .format())
        print(
            "Enchanté {0} {1}, je te souhaite une belle journée." 
            .format(FirstName, LastName))


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

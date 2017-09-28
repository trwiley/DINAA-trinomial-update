# Name: trinomialsplit.py
# Description: class that stores an ST and its split-up version
# Attributes:
#   Variables:
#       trinomial - string containing an instance of an ST.
#       statenumber - contains the state code. 1 - 50, alphabetical except for Alaska and Hawaii
#       countycode - contains alphabetical county code string.
#       sitenumber - contains actual site number.#

class TrinomialSplit:

    trinomial = ""
    statenumber = ""
    countycode = ""
    sitenumber = ""
    count = 0
    countycount = 0


    def __init__(self, trinomialinstance):
        self.trinomial = trinomialinstance
        self.split_trinomial()



    # see if the trinomial has dashes or spaces
    def has_dashes_or_spaces(self):
        for i in range(0, len(self.trinomial)):
            if (self.trinomial[i] == " ") or (self.trinomial[i] == "-"):
                return True

        return False

    def has_state_no(self):
        if self.trinomial[0].isdigit():
            return True
        else:
            return False

    # strip dashes or spaces
    def strip_dashes(self):
        strippedtrinomial = ""
        for i in range(0, len(self.trinomial)):
            # if the character is not a space or dash, copy it over.
            if (self.trinomial[i] != " ") and (self.trinomial[i] != "-"):
                strippedtrinomial += self.trinomial[i]
        self.trinomial = strippedtrinomial

    # see if the trinomial has parentheses or brackets, return true if the case.
    def has_parens_or_brackets(self):
        if (self.trinomial[0] == "(") and (self.trinomial[len(self.trinomial) - 1] == ")"):
            return True
        elif (self.trinomial[0] == "[") and (self.trinomial[len(self.trinomial) - 1] == "]"):
            return True
        else:
            return False

    # Strip trinomial of brackets or parens
    def strip_parens(self):
        strippedtrinomial = ""
        for i in range(0, len(self.trinomial)):
            # If not the first or last character (the spaces, in other words), copy over.
            if (i != 0) and (i != len(self.trinomial) - 1):
                strippedtrinomial += self.trinomial[i]

        # store the stripped version back into the original.
        self.trinomial = strippedtrinomial


    #Grabs the state code

    def get_state_code(self):
        for i in range(0, len(self.trinomial)):
            if self.trinomial[i].isdigit():
                self.statenumber += self.trinomial[i]
                self.count += 1
            elif self.count > 2:
                print("WARNING: state numbers are not more than 2 digits long. Have you checked if your data is "
                      "cleaned?")
                return
            else:
                return

    #Grabs the county code
    def get_county_code(self):
        for i in range(len(self.statenumber), len(self.trinomial)):
            if self.trinomial[i].isalpha():
                self.countycode += self.trinomial[i]
                self.count += 1
                self.countycount += 1
            elif self.countycount > 3:
                print("WARNING: county codes are typically not more than 3 digits long. Have you checked if your data "
                      "is cleaned?")
                return
            else:
                return


    #grabs the site number
    def get_site_number(self):
        for i in range(self.count, len(self.trinomial)):
            self.sitenumber += self.trinomial[i]

    # see if the site number has leading zeros
    def has_leading(self):
        if self.sitenumber[0] == "0":
            return True
        else:
            return False

    #count and return the number of leading zeros
    def leadingzeros(self):
        leading = 0
        for i in range(0, len(self.sitenumber)):
            if self.sitenumber[i] == "0":
                leading += 1
            else:
                return leading

    # remove the leading zeroes
    def remove_leading(self):
        temp = ""
        # start counting at the point where there are no leading zeroes.
        for i in range(self.leadingzeros(), len(self.sitenumber)):
            temp += self.sitenumber[i]
        self.sitenumber = temp




    def split_trinomial(self):

        if self.has_parens_or_brackets():
            self.strip_parens()

        if self.has_dashes_or_spaces():
            self.strip_dashes()

        if self.is_lowercase():
            self.change_toupper()

        if self.has_state_no():
             self.get_state_code()
        else:
            self.statenumber = "00"
        self.get_county_code()
        self.get_site_number()

        if self.has_leading():
            self.remove_leading()


    # Test function to print out the trinomial elements.
    def print_elements(self):
        print(self.statenumber + " " + self.countycode + " " + self.sitenumber)
     # test function
    def print_trinomial(self):
        print(self.trinomial)

    # checks if any of the letters are lower case, and, if so, returns true.
    def is_lowercase(self):
        for i in range(0, len(self.trinomial)):
            if self.trinomial[i].isalpha():
                if self.trinomial.islower():
                    return True

        return False

    #changes any lowercase letters to uppercase.
    def change_toupper(self):
        temp = ""
        for i in range(0, len(self.trinomial)):
            if  self.trinomial[i].isalpha() and self.trinomial[i].islower():
                temp += self.trinomial[i].upper()
            else:
                temp += self.trinomial[i]
        self.trinomial = temp
        
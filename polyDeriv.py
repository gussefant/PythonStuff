# Polynom function derivater
# By Kevin Christiansen Balouch
# GitHub: https://github.com/kevinbalouch
# This work is licensed under GNU GPL v2.0 (http://www.gnu.org/licenses/gpl-2.0.html)
#
# Note: This is work is unfinished, and negative exponations will not
# work, for now.

polyInput = int(
    input('Enter the highest exponation in the polynomal function: '))
polyDerivated = ""


def findDeriv(base, exp, be): #returns a processed array[nBase, nPoly, b or e (return base or exponent)]
    if (base != 0):
        nPoly = [base * exp, exp - 1]  # [prossedBase, processedExponent]

        if (be == "b"):
            return nPoly[0]
        elif (be == "e"):
            return nPoly[1]
    else:
        return 0


# Reversed for mathematicaly correct order. Higher to lower exponent. 1+
# for ending at 0.
for num in reversed(range(1, polyInput + 1)):
    baseInput = int(
        input('Enter the x value of x*n^%d (Type 0 if not present in function): ' % num))
    calcBase = findDeriv(baseInput, num, "b")  # num = exponent.
    calcExp = findDeriv(baseInput, num, "e")

    if (calcBase == 0):
        polyDerivated = polyDerivated
    else:
        if (calcExp == 0):
            polyDerivated = polyDerivated + "+ " + str(calcBase)
        else:
            strPoly = str(calcBase) + "x^" + str(calcExp) + " "
            polyDerivated = polyDerivated + strPoly

print(str(polyDerivated))

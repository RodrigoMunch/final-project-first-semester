

from generalfunctions import projectdetails
from arquivefunctions import setfiles, importcarsbd, importclientsbd, importaddressbd, importrentbd
from menu import menu

setfiles()
carsbd = importcarsbd()
clientsbd = importclientsbd()
addressbd = importaddressbd()
rentbd = importrentbd()



if __name__ == '__main__':
    projectdetails()
    menu()

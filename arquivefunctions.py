

def setfiles():
    carsbd = 'carsbd.txt'
    clientsbd = 'clientsbd.txt'
    addressbd = 'addressbd.txt'
    rentbd = 'rentbd.txt'
    try:
        #   carsbd
        file = open(carsbd, 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open(carsbd, 'wt+', encoding='utf-8')
            file.close()
        except:
            print(f'Houve um Erro na Criação do Arquivo: "{carsbd}"')

    try:
        #   clientsbd
        file = open(clientsbd, 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open(clientsbd, 'wt+', encoding='utf-8')
            file.close()
        except:
            print(f'Houve um Erro na Criação do Arquivo: "{clientsbd}"')

    try:
        #   addressbd
        file = open(addressbd, 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open(addressbd, 'wt+', encoding='utf-8')
            file.close()
        except:
            print(f'Houve um Erro na Criação do Arquivo: "{addressbd}"')

    try:
        file = open(rentbd, 'rt', encoding='utf-8')
        file.close()
    except FileNotFoundError:
        try:
            file = open(rentbd, 'wt+', encoding='utf-8')
            file.close()
        except:
            print(f'Houve um Erro na Criação do Arquivo: "{rentbd}"')



def importcarsbd():
    import pickle, os.path
    carsbd = 'carsbd.txt'
    if os.path.getsize(carsbd) > 0:
        with open(carsbd, 'rb') as a:
            return pickle.load(a)
    else:
        return []


def importclientsbd():
    import pickle, os.path
    clientsbd = 'clientsbd.txt'
    if os.path.getsize(clientsbd) > 0:
        with open(clientsbd, 'rb') as a:
            return pickle.load(a)
    else:
        return []


def importaddressbd():
    import pickle, os.path
    addressbd = 'addressbd.txt'
    if os.path.getsize(addressbd) > 0:
        with open(addressbd, 'rb') as a:
            return pickle.load(a)
    else:
        return []


def importrentbd():
    import pickle, os.path
    rentbd = 'rentbd.txt'
    if os.path.getsize(rentbd) > 0:
        with open(rentbd, 'rb') as a:
            return pickle.load(a)
    else:
        return []




if __name__ == '__main__':
    pass




#%%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """ descrição como funciona a função
    """
    return aporte * (1+ taxa) ** anos


#%%

juros_compostos(1200, 0.13, 1)

juros_compostos(aporte=1200, taxa=0.13, anos=1)

juros_compostos()
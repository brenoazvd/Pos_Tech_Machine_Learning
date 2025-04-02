def calcular_retorno_investimento(valor_inicial, valor_final):
    retorno = (valor_final - valor_inicial) / valor_inicial * 100
    return retorno

#valor_inicial = 1000
#valor_final = 1200

#retorno = calcular_retorno_investimento(valor_inicial, valor_final)
#print(f"Retorno do investimento: {retorno:.2f}%")

def calcular_juros_compostos(principal, taxa_juros_anual, periodos):
    taxa_juros_decimal = taxa_juros_anual /100
    valor_final = principal*(1 + taxa_juros_decimal) ** periodos
    return valor_final

def converter_taxa_anual_para_mensal(taxa_anual):
    taxa_mensal = (1 +taxa_anual/100)** (1/12) - 1
    return taxa_mensal ** 100

def calcular_cagr(valor_inicial, valor_final, anos): 
    cagr = ((valor_final / valor_inicial)** (1/anos)-1 )* 100
    return cagr 
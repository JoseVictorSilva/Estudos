import Orange

base_risco_credito = Orange.data.Table('../Arquivos Base/risco_credito_regras.csv')
print(base_risco_credito.domain)
cn2 = Orange.classification.rules.CN2Learner()
regras_riscos_credito = cn2(base_risco_credito) # cria as regras

for regras in regras_riscos_credito.rule_list:
    print(regras)

# História boa = 0; desconhecia = 1; ruim = 2
# Dívida alta = 0; baixa = 1;
# Garantia adequada = 0; nenhuma = 1
# Renda 0_15 = 0; 15_35 = 1; acima_35 = 2

# História boa(0), dívida alta(0), garantia nenhuma(1), renda > 35(2) -> resultado é baixo
# História ruim(2), dívida alta(0), garantia adequada(0), renda < 15(0) -> resultado moderado

previsoes = regras_riscos_credito(['boa','alta','nenhuma','acima_35'],['ruim','alta','adequada','0_15'])
print(previsoes) # sai array([1,0]) -> alto e baixo
print(base_risco_credito.domain.class_var.values) # mostra as classes

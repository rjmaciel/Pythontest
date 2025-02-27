print("Este programa cálcula o salário liquido em Portugal no ano de 2025, para não casados com 0 dependentes")
Vencimento_base_bruto = float(input('Qual seu vencimento base mensal bruto?: '))
Dias_uteis_trabalhados = float(input('Quantos dias uteis voce trabalhou este mês?: '))
Valor_diário_refeição = float(input('Qual o valor diário do seu subsidio de refeição?: '))
Num_horas_noturnas = float(input('Quantas horas noturnas voce fez este mês?: '))
Ajudas_de_custo_dedutiveis_nao_dedutiveis = float(input('Qual o valor TOTAL que recebe em ajudas de custos não dedutiveis de SS e IRS?: '))
Ajudas_de_custo_dedutiveis = float(input('Qual o valor TOTAL que recebe em ajudas de custos dedutiveis de SS e IRS? (Exemplos: Subsidios de turno/laboratorio/home office/subsidio de transporte/isenção de horario): '))
Duodecimos = input('Voce recebe duodecimos juntamente com o salario?: ')
Subsidio_alimentação = Dias_uteis_trabalhados * Valor_diário_refeição
Valor_hora = (Vencimento_base_bruto * 12)/(52*40)
Valor_hora_noturna = Valor_hora * 1.25
a_receber_horas_noturnas = Num_horas_noturnas * Valor_hora_noturna
Isento = input('Voce está isento de SS?: ')
respostas_isento = 'sim' , 's' , 'SIM' , 'S' , 'Y' , 'YES' , 'y' , 'yes' 
Vencimento_bruto_total = Vencimento_base_bruto + a_receber_horas_noturnas + Ajudas_de_custo_dedutiveis
# Condições de descontos para a SS, se o vbb for menor ou igual a 870€ E isento, o desconto é 0
if Vencimento_bruto_total <= 870 and Isento.lower() in respostas_isento:
    Desconto_SS = 0
else: Desconto_SS = Vencimento_bruto_total * 0.11
# Condições da tabela de IRS, consoante o valor do salário bruto vai corresponder a um escalão de IRS
if Vencimento_bruto_total <= 870:
    Descontos_IRS = 0
elif Vencimento_bruto_total <= 992:
    Descontos_IRS = 0.1300 * 2.60 * (1208.32 - Vencimento_bruto_total)
elif Vencimento_bruto_total <= 1070:
    Descontos_IRS = 0.1650 * 1.35 * (1477.67 - Vencimento_bruto_total)
elif Vencimento_bruto_total <= 1136:
    Descontos_IRS = (Vencimento_bruto_total * 0.1650) - 90.81
elif Vencimento_bruto_total <= 1187:
    Descontos_IRS = (Vencimento_bruto_total * 0.2200) - 153.29
elif Vencimento_bruto_total <= 1787:
    Descontos_IRS = (Vencimento_bruto_total * 0.2500) - 188.90
elif Vencimento_bruto_total <= 2078:
    Descontos_IRS = (Vencimento_bruto_total * 0.3200) - 313.99
elif Vencimento_bruto_total <= 2432:
    Descontos_IRS = (Vencimento_bruto_total * 0.3550) - 386.72
elif Vencimento_bruto_total <= 3233:
    Descontos_IRS = (Vencimento_bruto_total * 0.3872) - 465.03
elif Vencimento_bruto_total <= 5547:
    Descontos_IRS = (Vencimento_bruto_total * 0.4005) - 508.03
elif Vencimento_bruto_total <= 20221:
    Descontos_IRS = (Vencimento_bruto_total * 0.4495) - 779.83 
else:
    Descontos_IRS = (Vencimento_bruto_total * 0.4717) - 1228.74
Vencimento_liquido = Vencimento_bruto_total + Subsidio_alimentação + Ajudas_de_custo_dedutiveis_nao_dedutiveis - Desconto_SS - Descontos_IRS
print("Seu salário liquido é de", Vencimento_liquido, "€")
# horas extra, turnos extra e duodecimos!?!?!
# Na realidade só adicionei esta linha de comentário neste ficheiro, para testar no GitHub!
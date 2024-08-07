from handlers.generation_handler import generar_valor_polinomico


for i in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
    print(i, round(generar_valor_polinomico(10000, i), 2))    
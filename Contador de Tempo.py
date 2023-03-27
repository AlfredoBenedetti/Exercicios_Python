import time

# Define a quantidade de segundos que o contador irá rodar
tempo_total = 10

# Inicia o contador de tempo
start_time = time.time()

# Loop while que roda até atingir o tempo total
while (time.time() - start_time) < tempo_total:
    segundos_decorridos = int(time.time() - start_time)
    print("Segundos decorridos:", segundos_decorridos)
    time.sleep(1)  # Aguarda 1 segundo antes de continuar o loop

print("Contador finalizado.")

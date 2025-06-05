# Programa 9.11: Exibindo componentes da data e hora

import time

agora = time.localtime()

print(f"ANO:{agora.tm_year} ")
print(f"MES:{agora.tm_mon} ")
print(f"DIA:{agora.tm_mday} ")
print(f"HORA: {agora.tm_hour}")
print(f"MINUTO: {agora.tm_min}")
print(f"SEGUNDO: {agora.tm_sec}")
print(f"DIA DA SEMANA: {agora.tm_wday}")
print(f"DIA DO ANO: {agora.tm_yday}")
print(f"HORARIO DE VERÃO:{agora.tm_isdst} ")

print(time.strftime("%a %d/%m/%y %H%M", agora))

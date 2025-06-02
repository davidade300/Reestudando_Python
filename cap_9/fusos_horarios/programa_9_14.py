from datetime import datetime
from zoneinfo import ZoneInfo

bruxelas = ZoneInfo("Europe/Brussels")
nova_iorque = ZoneInfo("America/New_York")
tokio = ZoneInfo("Japan")
manaus = ZoneInfo("America/Manaus")
brasilia = ZoneInfo("Brazil/East")
rio_branco = ZoneInfo("America/Rio_Branco")

agora = datetime.now()

print("Agora em: ")
print("Bruxelas ", agora.astimezone(bruxelas))
print("Nova Iorque ", agora.astimezone(nova_iorque))
print("Tokio  ", agora.astimezone(tokio))
print("\nAgora no Brasil: ")
print("Rio Branco: ", agora.astimezone(rio_branco))
print("Manaus  ", agora.astimezone(manaus))
print("Brasilia   ", agora.astimezone(brasilia))

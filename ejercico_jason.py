import json

# Simulación de respuesta cruda obtenida desde una API RESTful de red
json_response = """
{
    "device": "Core-Router-01",
    "status": "active",
    "interfaces": [
        {
            "name": "GigabitEthernet0/0",
            "ip": "192.168.1.1",
            "netmask": "255.255.255.0",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/1",
            "ip": "10.0.0.1",
            "netmask": "255.255.255.252",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/2",
            "ip": "unassigned",
            "netmask": "none",
            "status": "down"
        }
    ]
}
"""

# 1. Deserializar la cadena JSON a un diccionario de Python
data = json.loads(json_response)

print(f"=== REPORTE DEL DISPOSITIVO: {data['device']} ===")
print(f"Estado General: {data['status']}\n")

# 2. Extraer y filtrar interfaces activas e IP asignadas
print("Interfaces Configuradas y Activas:")

for iface in data['interfaces']:
    if iface['status'] == 'up':
        print(
            f" - Interface: {iface['name']} | "
            f"IP: {iface['ip']} | "
            f"Estado: {iface['status']}"
        )

# 3. Serializar un nuevo objeto estructurado para exportación
nuevo_dispositivo = {
    "device": data['device'],
    "active_ips": [
        iface['ip']
        for iface in data['interfaces']
        if iface['status'] == 'up'
    ]
}

json_output = json.dumps(nuevo_dispositivo, indent=4)

print("\n=== JSON SERIALIZADO REESTRUCTURADO ===")
print(json_output)


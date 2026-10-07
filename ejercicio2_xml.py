import xml.etree.ElementTree as ET

# Cargar y parsear el archivo XML
tree = ET.parse("dispositivos.xml")
root = tree.getroot()

print("Root Tag:", root.tag)

# Recorrer la jerarquía XML
for router in root.findall("router"):

    router_id = router.attrib.get("id")
    hostname = router.find("hostname").text
    location = router.find("location").text

    print(f"\nRouter ID: {router_id} | Hostname: {hostname} | Ubicación: {location}")
    print("Interfaces:")

    # Buscar todas las interfaces
    for iface in router.find("interfaces").findall("interface"):

        nombre = iface.attrib.get("name")
        ip = iface.find("ip").text
        estado = iface.find("status").text

        print(f" * {nombre} -> IP: {ip} | Estado: {estado}")
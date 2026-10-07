import xml.etree.ElementTree as ET
import json

def xml_a_json_rutas(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except FileNotFoundError:
        return f"Error: El archivo '{xml_file}' no existe en esta carpeta."
    except ET.ParseError:
        return f"Error: El archivo '{xml_file}' está vacío o tiene un error de sintaxis XML."

    rutas_list = []

    # Extraer cada ruta del XML de forma segura
    for route in root.findall('route'):
        # Buscamos los nodos individualmente para evitar errores si falta alguno
        dest = route.find('destination')
        next_hop = route.find('next_hop')
        protocol = route.find('protocol')
        metric = route.find('metric')

        # Convertimos la métrica a entero solo si el nodo existe y tiene un número
        if metric is not None and metric.text and metric.text.isdigit():
            metrica_val = int(metric.text)
        else:
            metrica_val = 0

        item = {
            "destino": dest.text if dest is not None else "N/A",
            "siguiente_salto": next_hop.text if next_hop is not None else "N/A",
            "protocolo": protocol.text if protocol is not None else "N/A",
            "metrica": metrica_val
        }
        rutas_list.append(item)

    # Construir objeto normalizado
    json_normalizado = {
        "tabla_enrutamiento": {
            "total_rutas": len(rutas_list),
            "rutas": rutas_list
        }
    }

    return json.dumps(json_normalizado, indent=4, ensure_ascii=False)

# Ejecución y visualización del resultado
# Cambia 'routing_table.xml' por el nombre real de tu archivo si es diferente
archivo_xml = 'routing_table.xml' 
json_resultado = xml_a_json_rutas(archivo_xml)

# Si la función devolvió un error de archivo, lo imprimimos y detenemos
if json_resultado.startswith("Error:"):
    print(json_resultado)
else:
    print("=== TABLA DE ENRUTAMIENTO EN JSON NORMALIZADO ===")
    print(json_resultado)

    # Guardar en archivo resultado.json
    with open('routing_table_normalized.json', 'w', encoding='utf-8') as f:
        f.write(json_resultado)
    print("\n¡Archivo 'routing_table_normalized.json' generado con éxito!")

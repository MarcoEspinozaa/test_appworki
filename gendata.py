
#Se creó este script con la sugerencia de un potencial bloqueo por ip antes 
#tantas consultas y se guardó la data dentro del proyecto.
import json

data = [
    {
    "Fecha": "2022-04-28 12:40:01",
    "Latitud": "-30.143",
    "Longitud": "-72.206",
    "Profundidad": "31.8",
    "Magnitud": "3.1 Ml",
    "Agencia": "GUC",
    "RefGeografica": "70 km al O de Tongoy",
    "FechaUpdate": "2022-04-28T13:05:00.580Z"
  },
  {
    "Fecha": "2022-04-28 12:18:44",
    "Latitud": "-21.232",
    "Longitud": "-67.597",
    "Profundidad": "211.8",
    "Magnitud": "4.2 Ml",
    "Agencia": "GUC",
    "RefGeografica": "68 km al E de Ollagüe",
    "FechaUpdate": "2022-04-28T13:05:00.580Z"
  },
  {
    "Fecha": "2022-04-28 12:00:40",
    "Latitud": "-21.920",
    "Longitud": "-68.730",
    "Profundidad": "117.6",
    "Magnitud": "3.0 Ml",
    "Agencia": "GUC",
    "RefGeografica": "65 km al N de Calama",
    "FechaUpdate": "2022-04-28T13:05:00.583Z"
  },
  {
    "Fecha": "2022-04-28 07:39:12",
    "Latitud": "-23.884",
    "Longitud": "-67.036",
    "Profundidad": "229.2",
    "Magnitud": "3.5 Ml",
    "Agencia": "GUC",
    "RefGeografica": "93 km al E de Socaire",
    "FechaUpdate": "2022-04-28T13:05:00.583Z"
  },
  {
    "Fecha": "2022-04-28 07:21:26",
    "Latitud": "-30.293",
    "Longitud": "-71.255",
    "Profundidad": "50.9",
    "Magnitud": "2.9 Ml",
    "Agencia": "GUC",
    "RefGeografica": "18 km al O de Andacollo",
    "FechaUpdate": "2022-04-28T13:05:00.583Z"
  },
  {
    "Fecha": "2022-04-28 06:46:46",
    "Latitud": "-21.466",
    "Longitud": "-68.518",
    "Profundidad": "133.0",
    "Magnitud": "2.9 Ml",
    "Agencia": "GUC",
    "RefGeografica": "38 km al SO de Ollagüe",
    "FechaUpdate": "2022-04-28T13:05:00.583Z"
  },
  {
    "Fecha": "2022-04-28 05:07:25",
    "Latitud": "-23.925",
    "Longitud": "-67.634",
    "Profundidad": "268.5",
    "Magnitud": "2.7 Ml",
    "Agencia": "GUC",
    "RefGeografica": "45 km al SE de Socaire",
    "FechaUpdate": "2022-04-28T13:05:00.587Z"
  },
  {
    "Fecha": "2022-04-28 01:14:06",
    "Latitud": "-20.789",
    "Longitud": "-68.875",
    "Profundidad": "99.2",
    "Magnitud": "4.0 Ml",
    "Agencia": "GUC",
    "RefGeografica": "23 km al O de Mina Collahuasi",
    "FechaUpdate": "2022-04-28T13:05:00.587Z"
  },
  {
    "Fecha": "2022-04-28 00:34:37",
    "Latitud": "-20.772",
    "Longitud": "-70.783",
    "Profundidad": "22.8",
    "Magnitud": "3.0 Ml",
    "Agencia": "GUC",
    "RefGeografica": "90 km al SO de Iquique",
    "FechaUpdate": "2022-04-28T13:05:00.587Z"
  },
  {
    "Fecha": "2022-04-27 23:00:21",
    "Latitud": "-18.314",
    "Longitud": "-69.828",
    "Profundidad": "87.1",
    "Magnitud": "2.8 Ml",
    "Agencia": "GUC",
    "RefGeografica": "31 km al SO de Putre",
    "FechaUpdate": "2022-04-28T13:05:00.587Z"
  },
  {
    "Fecha": "2022-04-27 22:30:48",
    "Latitud": "-29.597",
    "Longitud": "-71.454",
    "Profundidad": "69.9",
    "Magnitud": "3.7 Ml",
    "Agencia": "GUC",
    "RefGeografica": "26 km al O de La Higuera",
    "FechaUpdate": "2022-04-28T13:05:00.587Z"
  },
  {
    "Fecha": "2022-04-27 21:44:52",
    "Latitud": "-20.187",
    "Longitud": "-69.015",
    "Profundidad": "105.4",
    "Magnitud": "3.4 Ml",
    "Agencia": "GUC",
    "RefGeografica": "47 km al NE de Pica",
    "FechaUpdate": "2022-04-28T13:05:00.590Z"
  },
  {
    "Fecha": "2022-04-27 20:02:13",
    "Latitud": "-32.612",
    "Longitud": "-71.733",
    "Profundidad": "31.4",
    "Magnitud": "3.2 Ml",
    "Agencia": "GUC",
    "RefGeografica": "50 km al N de Valparaíso",
    "FechaUpdate": "2022-04-28T13:05:00.590Z"
  },
  {
    "Fecha": "2022-04-27 18:18:28",
    "Latitud": "-21.154",
    "Longitud": "-68.871",
    "Profundidad": "112.6",
    "Magnitud": "2.9 Ml",
    "Agencia": "GUC",
    "RefGeografica": "43 km al SO de Mina Collahuasi",
    "FechaUpdate": "2022-04-28T13:05:00.590Z"
  },
  {
    "Fecha": "2022-04-27 17:04:25",
    "Latitud": "-21.233",
    "Longitud": "-68.521",
    "Profundidad": "130.4",
    "Magnitud": "2.7 Ml",
    "Agencia": "GUC",
    "RefGeografica": "28 km al O de Ollagüe",
    "FechaUpdate": "2022-04-28T13:05:00.590Z"
  }
]

with open("data.json","w") as outfile:
    outfile.write(json.dumps(data))
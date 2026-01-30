# ForSale

## 📌 Descripción

**ForSale.py** es un script en Python orientado al análisis estacional de activos financieros. Su objetivo principal es identificar **qué mes del año es históricamente más barato para comprar** y **qué mes es más caro para vender** un activo, utilizando datos históricos de precios.

El script forma parte del proyecto **pipfin** y está diseñado como herramienta de *research cuantitativo*, análisis de estacionalidad y backtesting de estrategias temporales.

---

## 🎯 Objetivo del sistema

Detectar patrones estacionales en activos financieros para:

* identificar oportunidades de compra
* identificar ventanas óptimas de venta
* analizar comportamiento histórico mensual
* construir estrategias basadas en calendario
* backtesting temporal

---

## ⚙️ Lógica técnica

El modelo realiza:

* descarga de datos históricos con `yfinance`
* resampleo mensual de precios de cierre
* cálculo de promedios históricos por mes
* detección del mes más barato (buy month)
* detección del mes más caro (sell month)
* simulación de retornos año por año

### Regla base

* Compra en mes históricamente más barato
* Venta en mes históricamente más caro

---

## ▶️ Ejecución

```bash
python ForSale.py
```

El sistema solicita por consola el ticker del activo:

```
Ingrese el ticker de la acción que quiere analizar (ejemplo: AAPL)
```

---

## 📈 Salida esperada

* mes históricamente más barato para comprar
* mes históricamente más caro para vender
* tabla de resultados anuales
* retornos por período
* retorno promedio anual
* retorno acumulado histórico

---

## 🧠 Aplicaciones

* trading estacional
* estrategias basadas en calendario
* research financiero
* análisis cuantitativo
* backtesting sistemático
* generación de modelos temporales

---

## 🏗️ Arquitectura

Script diseñado como:

* entrypoint independiente
* módulo reutilizable
* componente de sistema mayor
* base para automatización futura

---

## 🧑‍💻 Autor

Victor Daniel Nieto
Proyecto: **pipfin**

---

## 📄 Licencia

Uso privado / desarrollo interno

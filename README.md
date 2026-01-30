\# pipfin



\## 🧠 Plataforma de herramientas financieras en Python



\*\*pipfin\*\* es un proyecto orientado al desarrollo de herramientas de análisis financiero, trading cuantitativo y \*research\* de mercados utilizando Python como lenguaje base. El objetivo del repositorio es centralizar scripts, modelos y sistemas que permitan analizar activos financieros desde un enfoque técnico, estadístico y estacional.



---



\## 🎯 Objetivo del proyecto



Construir un ecosistema modular de herramientas financieras para:



\* análisis técnico

\* trading algorítmico

\* screening de mercados

\* research cuantitativo

\* backtesting de estrategias

\* análisis estacional

\* automatización de procesos financieros



---



\## 🧩 Componentes del sistema



\### 🔹 Top100MCRSI-30



Herramienta de \*screening\* basada en RSI (Relative Strength Index) para la detección automática de activos en \*\*zona de sobreventa (RSI ≤ 30)\*\* dentro de un universo Top 100.



Funciones principales:



\* cálculo de RSI

\* filtrado técnico

\* ranking de activos

\* generación de oportunidades



---



\### 🔹 ForSale



Sistema de análisis estacional orientado a identificar:



\* el mes históricamente más barato para comprar un activo

\* el mes históricamente más caro para venderlo



Funciones principales:



\* descarga de datos históricos

\* análisis mensual

\* promedios históricos por mes

\* backtesting temporal

\* simulación de retornos



---



\## ⚙️ Enfoque técnico



El proyecto se basa en principios de:



\* modularidad

\* escalabilidad

\* reutilización de código

\* separación de lógica

\* diseño de sistemas

\* arquitectura extensible



---



\## 🏗️ Arquitectura del repositorio



```txt

pipfin/

├── Top100MCRSI-30.py      # Screener RSI

├── ForSale.py             # Análisis estacional

├── README.md              # Documentación general

├── ReadMeTop100MCRSI-30.md

└── ReadMeForSale.md

```



---



\## ▶️ Ejecución



\### Screener RSI



```bash

python Top100MCRSI-30.py

```



\### Análisis estacional



```bash

python ForSale.py

```



---



\## 🧠 Aplicaciones



\* trading cuantitativo

\* trading algorítmico

\* análisis técnico sistemático

\* research financiero

\* automatización de estrategias

\* construcción de modelos financieros

\* sistemas de decisión



---



\## 🧩 Tecnologías utilizadas



\* Python

\* pandas

\* numpy

\* yfinance

\* análisis estadístico

\* procesamiento de datos



---



\## 📈 Filosofía del proyecto



pipfin no es un conjunto de scripts aislados, sino un \*\*ecosistema de herramientas financieras\*\* diseñado para crecer como plataforma:



\* nuevas estrategias

\* nuevos modelos

\* nuevos indicadores

\* nuevos sistemas

\* nuevos módulos

\* nuevas arquitecturas



---



\## 🧑‍💻 Autor



Victor Daniel Nieto



---



\## 📄 Licencia



Uso privado / desarrollo interno




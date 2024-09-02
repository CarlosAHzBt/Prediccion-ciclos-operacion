# Reporte Final: Predicción de la Vida Útil Remanente (RUL) en Motores

## Introducción

El objetivo de este proyecto es predecir la vida útil remanente (RUL) de motores de aeronaves utilizando datos sensoriales obtenidos durante su operación. La predicción precisa de la RUL es crucial para el mantenimiento predictivo, permitiendo programar reparaciones y prevenir fallas catastróficas en el equipo. Utilizamos un conjunto de datos proporcionado por la NASA que simula el desgaste y la degradación de los motores a lo largo del tiempo.

## Exploración de Datos (EDA)

Durante la fase de exploración de datos, analizamos las características de los datos sensoriales a lo largo del ciclo de vida de los motores. Se realizaron varias visualizaciones para entender la distribución de las características y cómo estas cambian con el tiempo.

### Visualización de Sensores

Las siguientes visualizaciones muestran cómo las lecturas de los sensores varían a lo largo del tiempo:

- **Figura 1:** Muestra la variabilidad de las características seleccionadas (Feature 0 a Feature 4) a lo largo de los ciclos.
- **Figura 2:** Representa todos los ciclos disponibles en el conjunto de datos, destacando la densidad de los datos y la fluctuación de las características.

Estas visualizaciones ayudaron a identificar patrones y tendencias en las lecturas de los sensores, fundamentales para la predicción precisa de la RUL.


## Preprocesamiento de Datos

El preprocesamiento de los datos incluyó las siguientes etapas:

1. **Carga de Datos:** Los datos crudos fueron cargados desde la carpeta `data/raw/`.
2. **Normalización:** Se aplicó normalización a las características sensoriales para asegurar que todas las características estuvieran en la misma escala.
3. **Selección de Características:** Se seleccionaron las características más relevantes para el modelo, basándonos en la exploración de datos y análisis de correlación.
4. **Guardado de Datos Procesados:** Los datos preprocesados fueron guardados en `data/processed/` para su uso en el modelado.


## Modelado

El modelo seleccionado para predecir la RUL fue un **Random Forest Regressor**, debido a su capacidad para manejar grandes volúmenes de datos y múltiples características sin requerir demasiada ingeniería de características previa.

### Proceso de Entrenamiento

1. **División de Datos:** Los datos preprocesados se dividieron en un conjunto de entrenamiento (80%) y un conjunto de prueba (20%).
2. **Entrenamiento del Modelo:** El modelo se entrenó utilizando el conjunto de entrenamiento y optimizando hiperparámetros como la cantidad de árboles en el bosque.
3. **Evaluación:** El modelo se evaluó utilizando el conjunto de prueba, y se calcularon las métricas de rendimiento (MSE y MAE).

Los parámetros óptimos se seleccionaron para maximizar la precisión del modelo mientras se minimizaban los errores de predicción.


## Resultados

### Métricas de Evaluación

El modelo fue evaluado utilizando las siguientes métricas:

- **Mean Squared Error (MSE):** 0.1745
- **Mean Absolute Error (MAE):** 0.2950

### Visualización de Resultados

La siguiente figura muestra la comparación entre las predicciones del modelo y los valores reales de RUL en el conjunto de prueba.

- **Figura 3:** Comparación entre las predicciones y los valores reales de RUL. La línea roja indica donde las predicciones coincidirían exactamente con los valores reales.

Estas métricas y visualizaciones indican que el modelo tiene un buen rendimiento en la predicción de la RUL, aunque hay margen para mejoras.


## Conclusiones y Próximos Pasos

El modelo de Random Forest Regressor demostró ser efectivo en la predicción de la vida útil remanente de motores de aeronaves, como lo indican las bajas métricas de error (MSE y MAE). Sin embargo, hay espacio para mejorar:

- **Optimización de Hiperparámetros:** Realizar una búsqueda más exhaustiva de hiperparámetros podría mejorar aún más el rendimiento.
- **Modelos Avanzados:** Probar con modelos más avanzados como Gradient Boosting Machines o redes neuronales profundas.
- **Ensamblaje de Modelos:** Combinar diferentes modelos podría reducir aún más los errores de predicción.

Este proyecto establece una base sólida para futuras investigaciones y mejoras en el campo del mantenimiento predictivo de motores.

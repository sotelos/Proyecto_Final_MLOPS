# Proyecto Final MLOps - Predicción de Seguros Médicos

Este proyecto implementa un pipeline industrializado de Machine Learning con automatización CI/CD, enfocado en la predictibilidad, auditabilidad y gobernanza de modelos bajo estándares profesionales.

## 📊 Descripción del Dataset
Para este proyecto se seleccionó el **Medical Cost Personal Dataset** (fuente externa).
- **Contexto:** El dataset contiene datos históricos de beneficiarios de seguros de salud.
- **Variables:** Incluye características demográficas y de salud como edad, sexo, índice de masa corporal (BMI), número de hijos, condición de fumador y región geográfica.
- **Objetivo (Target):** Predecir el costo de la prima del seguro (`charges`).

## 🛠️ Estructura del Proyecto
- `src/train.py`: Orquestador de entrenamiento y tracking con MLflow.
- `Makefile`: Automatización de tareas de ingeniería (install, lint, test, train).
- `.github/workflows/ml.yml`: Pipeline de Integración Continua (CI).

## 📈 Métricas de Evaluación y Justificación
Se han seleccionado las siguientes métricas para evaluar el desempeño del modelo de regresión:

1. **MSE (Mean Squared Error):** Mide el promedio de los errores al cuadrado. Se utiliza para penalizar errores grandes, lo cual es crítico en seguros para evitar subestimaciones graves de costos.
2. **RMSE (Root Mean Squared Error):** Facilita la interpretación al estar en las mismas unidades que la variable objetivo (USD).
3. **MAE (Mean Absolute Error):** Proporciona el error promedio absoluto, ofreciendo una visión clara de la desviación típica en cada predicción.
4. **R² (Coeficiente de Determinación):** Indica qué porcentaje de la variabilidad de los costos es explicada por el modelo. Es nuestra métrica de referencia para la precisión del baseline.

## ⚙️ Comandos de Automatización
El proyecto utiliza un Makefile para garantizar la repetibilidad del entorno:
- `make install`: Instalación de dependencias.
- `make lint`: Verificación de calidad y estilo de código.
- `make test`: Pruebas de integridad de la estructura del proyecto.
- `make train`: Ejecución del pipeline de ML y registro en MLflow.

## 🛡️ Gobernanza y CI/CD
Cada cambio en el código dispara un flujo en **GitHub Actions** que:
1. Valida el entorno y la calidad del código.
2. Entrena el modelo y registra parámetros, métricas y la **Firma del Modelo (Signature)** en MLflow.
3. Genera un **Artefacto** descargable con la evidencia completa del experimento, asegurando la trazabilidad total del ciclo de vida del modelo.
# Comandos para automatización
install:
	pip install -r requirements.txt

train:
	python src/train.py

clean:
	powershell -Command "Remove-Item -Recurse -Force mlruns, mlartifacts, src/__pycache__"

test:
	# Verificación básica de la existencia de archivos críticos
	python -c "import os; assert os.path.exists('src/train.py'), 'Error: Script de entrenamiento no encontrado'"
	python -c "import os; assert os.path.exists('requirements.txt'), 'Error: Archivo de dependencias no encontrado'"
lint:
	# Verificación de sintaxis básica
	pip install flake8
	flake8 src/train.py --count --select=E9,F63,F7,F82 --show-source --statistics
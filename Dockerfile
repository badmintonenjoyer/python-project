# Używamy oficjalnego obrazu Pythona
FROM python:3.10-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki projektu do kontenera
COPY . /app

# Instalujemy zależności
RUN pip install --upgrade pip
RUN pip install pytest flake8

# Domyślna komenda (możesz ją zmienić)
CMD ["python", "--version"]

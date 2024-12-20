FROM python:3.9-slim

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Criar e definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY . .

# Criar diretórios necessários
RUN mkdir -p /app/media /app/static /app/staticfiles

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor a porta
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "cct.wsgi:application", "--bind", "0.0.0.0:8000"]

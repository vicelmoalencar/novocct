# Use uma imagem base Python oficial
FROM python:3.9

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
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
RUN mkdir -p /app/staticfiles /app/media
RUN python manage.py collectstatic --noinput

# Expor a porta
EXPOSE 3000

# Copiar script de entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Definir entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "3", "--timeout", "120", "cct.wsgi:application"]

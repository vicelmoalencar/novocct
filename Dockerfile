# Use uma imagem base Python oficial
FROM python:3.9-slim

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Criar e definir o diretório de trabalho
WORKDIR /app

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

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]

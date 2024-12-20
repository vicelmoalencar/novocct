#!/bin/sh

# Esperar pelo banco de dados
echo "Waiting for database..."
while ! nc -z $POSTGRES_HOST 5432; do
    sleep 1
done
echo "Database is ready!"

# Aplicar migrações
echo "Applying migrations..."
python manage.py migrate --noinput

# Executar o comando passado para o container
exec "$@"

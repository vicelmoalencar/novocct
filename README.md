# CCT EAD - Sistema de Ensino à Distância

Sistema de ensino à distância desenvolvido para o CCT, permitindo a criação e gerenciamento de cursos online, com suporte a vídeos, textos e avaliações.

## Configuração no EasyPanel

### 1. Serviço do Banco de Dados (PostgreSQL)

Crie um novo serviço para o banco de dados:
- Nome: `cct-db`
- Imagem: `postgres:13`
- Variáveis de Ambiente:
  ```
  POSTGRES_DB=cct
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=qaz123wsx
  ```
- Volume: `/var/lib/postgresql/data`

### 2. Serviço da Aplicação Django

Configure o serviço principal:
- Nome: `cct-ead`
- Variáveis de Ambiente:
  ```
  DJANGO_SECRET_KEY=django-insecure-5na2o8-+ri!1_#c*bg9js(*3)bg7g!p8)8=6(&%bhn0uu-17c3
  DJANGO_DEBUG=False
  ALLOWED_HOSTS=*
  POSTGRES_DB=cct
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=qaz123wsx
  POSTGRES_HOST=cct-db
  ```

### 3. Inicialização

Após configurar os serviços:
1. Inicie o serviço `cct-db`
2. Aguarde alguns segundos para o banco inicializar
3. Inicie o serviço `cct-ead`
4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

## Desenvolvimento Local

Para desenvolvimento local, use o Docker Compose:

```bash
docker-compose up -d
```

As mesmas variáveis de ambiente mencionadas acima devem ser configuradas em um arquivo `.env` na raiz do projeto.

## Funcionalidades

- Autenticação de usuários (alunos e instrutores)
- Gerenciamento de cursos e módulos
- Sistema de matrículas
- Acompanhamento de progresso
- Interface responsiva
- Editor de texto rico para conteúdo
- Sistema de avaliações
- Certificados de conclusão

## Tecnologias

- Django 4.2.7
- PostgreSQL
- Gunicorn
- Nginx
- Docker

## Requisitos

- Python 3.9+
- PostgreSQL
- Docker e Docker Compose (para produção)

## Configuração do Ambiente de Desenvolvimento

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cct-ead.git
cd cct-ead
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Copie o arquivo de exemplo de variáveis de ambiente:
```bash
cp .env.example .env
```

5. Configure as variáveis de ambiente no arquivo `.env`

6. Execute as migrações:
```bash
python manage.py migrate
```

7. Crie um superusuário:
```bash
python manage.py createsuperuser
```

8. Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Deploy com Docker

1. Configure as variáveis de ambiente no arquivo `.env`

2. Construa e inicie os containers:
```bash
docker-compose up -d --build
```

3. Execute as migrações:
```bash
docker-compose exec web python manage.py migrate
```

4. Crie um superusuário:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Manutenção

### Backup do Banco de Dados

```bash
docker-compose exec db pg_dump -U postgres cct > backup.sql
```

### Restauração do Banco de Dados

```bash
docker-compose exec -T db psql -U postgres cct < backup.sql
```

### Logs

```bash
docker-compose logs -f
```

## Segurança

- Todas as senhas são armazenadas com hash
- Proteção contra CSRF
- Configurações de segurança do Django ativadas
- HTTPS forçado em produção
- Headers de segurança configurados

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

## Suporte

Para suporte, envie um email para suporte@cct.com.br ou abra uma issue no GitHub.

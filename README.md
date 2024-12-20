# CCT EAD - Sistema de Ensino à Distância

Sistema de ensino à distância desenvolvido para o CCT, permitindo a criação e gerenciamento de cursos online, com suporte a vídeos, textos e avaliações.

## Funcionalidades

- Autenticação de usuários (alunos e instrutores)
- Gerenciamento de cursos e módulos
- Sistema de matrículas
- Acompanhamento de progresso
- Interface responsiva
- Editor de texto rico para conteúdo
- Sistema de avaliações
- Certificados de conclusão

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

## Deploy no EasyPanel

1. Faça login no EasyPanel

2. Crie um novo projeto

3. Configure as variáveis de ambiente:
   - DJANGO_SECRET_KEY
   - DB_PASSWORD
   - ALLOWED_HOSTS
   - EMAIL_HOST
   - EMAIL_PORT
   - EMAIL_HOST_USER
   - EMAIL_HOST_PASSWORD

4. Faça o deploy usando o Dockerfile e docker-compose.yml fornecidos

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

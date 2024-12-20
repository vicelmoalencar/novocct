# CCT - Sistema de Ensino a Distância

Sistema de ensino a distância desenvolvido com Django, oferecendo uma plataforma completa para educação online.

## Funcionalidades

- Autenticação de usuários (alunos, professores e administradores)
- Gerenciamento de cursos
- Sistema de aulas em vídeo
- Fórum de discussão
- Material didático
- Sistema de avaliação
- Certificados

## Requisitos

- Python 3.10+
- PostgreSQL
- Dependências listadas em requirements.txt

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/vicelmoalencar/novocct.git
cd novocct
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
DEBUG=True
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sua_url_do_banco
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Execute o servidor:
```bash
python manage.py runserver
```

## Deploy no EasyPanel

1. No EasyPanel, crie um novo projeto
2. Selecione o template Python/Django
3. Configure as variáveis de ambiente necessárias
4. Conecte ao repositório Git
5. Deploy!

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

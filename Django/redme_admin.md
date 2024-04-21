AD(Active Directory) e Django

pip install python-ldap
pip install django-auth-ldap

------------------------------------------------------------------------------------------
em paralelo o Django tem uma biblioteca que gerencia usuarios no banco interno do proprio django,
nao sei ainda em qual banco e se da pra escolher porem acessando a url/admin
de toda forma segue os procedimentos:

python manage.py migrate # para sincronizar as atualizações existente no banco de dados do Django
python manage.py makemigrations #
python manage.py createsuperuser # para criar um usuario admin no banco do Django. na configuração do arquivo urls.py

com isso ja conseguimos acessar a pagina admin: http://127.0.0.1:8000/admin/
path('admin/', admin.site.urls), deve esta antes do index. para acessar a pagina admin.

todo o esquema de permissões 


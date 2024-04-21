essa parte dera foco nas configurações de templates.

cada app vai ter seu arquivo urls.py, para isolar as url e nao ficar todas as rotas em setup.
entao o arquivo local de url.py referencia o metodo correspondente em views.py de cada app ja
em setup usaremos a biblioteca include() apontando para o local do arquivo urls.py dentro do app.
ex:
 path('', include('Galeria.urls'))
---------------------------------------------------------------------------------------------------

{% static %} é uma tag de template do Django que você usa em seus arquivos HTML para referenciar arquivos estáticos, como CSS, JavaScript e imagens.

Quando você usa {% static 'styles/style.css' %} dentro do atributo href, o Django substitui essa tag pelo caminho correto para o arquivo estático style.css em seu projeto.
Isso é útil porque o caminho para os arquivos estáticos pode variar dependendo do ambiente

por fim para rodar toda essas atualizações usamos o comando 
python manage.py collectstatic # faz o Django entender os endereçamentos criados dos arquivos staticos

dentro de cada link existente na pagina vamos ter que usar a seguinte sintaxe:
href="{% static '/styles/style.css' %}"
aspas dupla fora da chave seguido de porcentagem e o arquivo abisoluto em aspas simples.
-----------------------------------------------------------------------------------------------------
























Requisições HTML:
GET: O método GET é usado para solicitar dados do servidor. Quando um formulário é enviado usando GET, os dados do formulário são 
anexados à URL como uma string de consulta. Isso significa que os dados do formulário são visíveis na barra de endereços do navegador.
O método GET é adequado para solicitações que não alteram o estado do servidor, como pesquisas.
html
Copy code
<form method="GET" action="/search">
    <input type="text" name="q" placeholder="Pesquisar...">
    <button type="submit">Pesquisar</button>
</form>

POST: O método POST é usado para enviar dados para o servidor no corpo da requisição HTTP. Os dados do formulário não são visíveis 
na URL. O método POST é adequado para solicitações que podem alterar o estado do servidor, como enviar um formulário de login.
html
Copy code
<form method="POST" action="/login">
    <input type="text" name="username" placeholder="Usuário" required>
    <input type="password" name="password" placeholder="Senha" required>
    <button type="submit">Entrar</button>
</form>
PUT e DELETE: Embora menos comuns em formulários HTML, os métodos PUT e DELETE também são usados para enviar dados para o servidor.
 PUT é usado para atualizar recursos existentes, enquanto DELETE é usado para excluir recursos.

PATCH: O método PATCH é usado para fazer alterações parciais em um recurso. É semelhante ao PUT, mas em vez de substituir o recurso 
inteiro, ele apenas atualiza os campos especificados.

Além disso, é importante entender que os formulários HTML também possuem os atributos action, que especifica para onde os dados do 
formulário devem ser enviados, e method, que especifica o método de requisição a ser usado (GET, POST, etc.). Estes atributos 
são essenciais para definir como o formulário interage com o servidor.
Camanadas:

7 - Aplicação
6 - Apresentação
5 - Sessão
4 - Transporte
3 - Rede
2 - Ligação de dados
1 - Fisica

Protocolos de Redes: 

FTP, FTPS e SFTP --> são protocolos utilizado para enviar mensagens e fotos do cliente para o servidor. o FTP era muito usado antigamente ate mesmo em sites para quem enviava as solicitações para o servidor.
o FTPS é a mesma coisa do FTP porem encriptografado, usando uma camada de segurança que é o SSL ja a criptografia utilizada pelo SFTP usa o SSH.

SSL x SSH --> o SSH é um protocolo para realizar uma conexao criptografada e posibilita acesso remoto do dispositivo ao servidor.A principal diferença entre SSH vs SSL é que SSH é usado para criar um túnel seguro para outro computador a partir do qual você pode emitir comandos, transferir dados, etc. Na outra ponta, o SSL é usado para transferir dados com segurança entre duas partes – não permite que você emita comandos como você pode com o SSH

Telnet  --> permite comunicação de inteface de aplicações aos promts dos servidores.
IRC     --> sistema de bate-papo onde um cliente IRC tem que acessar um servidor IRC para criar uma sala de bate-papo.

XMPP: é o protocolo de comunicação aberta, utilizado por programas de comunicação como Whatsapp. Por sua facilidade, ele tem ganhado espaço em aplicações direcionadas à Internet das Coisas (IoT).

HTTP e HTTPS: o HTTP (HyperText Transfer Protocol) é o que é utilizado toda vez que se acessa um site. Não é necessário digitar “http://” a cada endereço que preenche na barra de endereço do navegador, porém, assim que a tecla Enter é clicada, ele é exibido

O TCP é o protocolo mais usado, pois oferece garantia na entrega dos pacotes entre um PC emissor e um PC receptor

arquitetura Cliente/Servidor --> é uma estrutura mais logica do que fisica. temos que levar em consideração isso pois um mesmo ambiente pode ser tando server quando client. o cliente é responsavel por tomar as ações nessa relação e serve como interfasse da rede e funções dos servidores ao usuarios.
servidores --> equipamentos mais parrudos fornecem serviços pre estabelecido com a nessecidade da aplicação. fornece esse serviço aos usuarios que nescecitam. atende a diversos clientes simutaneamente.
tipos de serviço de servidores: servidor de arquivo, redes, impressora etc.
-----------------------------------------------------------------------------------------------------
IaaS = infra estrutura como serviço = vc gerencia e configura o hardware, criação de maquina virtual.

PaaS = plataforma como serviço = focado no desenvolvimento de aplicatico, o gerenciamento da plataforma é realizado pelo provedor de nuvem.

SaaS = software como serviço = modelo de pago conforme o uso. onde os usuarios pagam pelo software que utilizam como um modelo de assinatura.

-----------------------------------------------------------------------------------------------------
elasticidade = capacidade de se adaptar a carga de trabalho nescessaria para atender a demanda com o aumento de recursos de forma instantanea e automatica.

escalabilidade = é um prerequisito para a elasticidade, o sistema so pode ter elasticidade se for escalavel pois para que possa ter a redução do consumo de recurso quanto o aumento do consumo de recursos dentro do que foi criado de capacidade maxima para o sistema

-----------------------------------------------------------------------------------------------------
MS(microsoft) EXCHANGE 

1. Rehosting ou nova hospedagem
so vai envolver elevar a pilha para que depois ela seja deslocada da hospedagem atual para a nuvem. Nessa primeira parte será transportado uma cópia exatamente igual do ambiente onde os dados se encontram sem realizar muitas alterações para obter o ROI mais rapidamente. As empresas que possuem uma cultura mais conservadora ou que não têm nenhum tipo de estratégia a longo prazo para aproveitar os recursos avançados da migração para a nuvem são as melhores e mais adequadas
2. Replatforming ou atualização de plataforma
Do mesmo modo que a variação na elevação e no deslocamento precisa de ajustes adicionais, a atualização de plataforma também precisará para otimizar o cenário para a nuvem. Lembrando que a arquitetura central das aplicações continua igual. Para as empresas que são conservadoras e que desejam criar uma confiança na nuvem, essa também é uma boa estratégia.
3. Repurchasing ou reaquisição
Reaquisição, ou melhor, migrar as aplicações para um novo produto procedente da nuvem, como migrar de CRM para Salesforce. Nesse caso, a equipe precisará ser treinada para utilizar a nova plataforma. A reaquisição é uma opção econômica, caso a empresa for migrar os dados de uma perspectiva antiga altamente personalizada.
4. Refactoring ou refatoração ou nova arquitetura
Refatoração, ou seja, reconstruir as aplicações do zero. Normalmente esse fato é incentivado por uma necessidade comercial de aproveitar os recursos de nuvem que não estão disponíveis no cenário atual, como o dimensionamento automático em nuvem ou computação sem servidor. Essa opção na maioria das vezes possui um valor mais elevado, porém, é a mais compatível pensando nas versões futuras.
5. Retiring ou descontinuação
Depois de avaliar a listagem de aplicações em relação à disponibilidade para a nuvem, é possível que algumas aplicações não sejam úteis. Quando isso acontece é possível desativá-las, o que gera uma economia resultante que pode impulsionar negócios para aplicações que estão prontas para a migração.
6. Retaining - Retenção
Ainda existem empresas que acreditam que a adoção da nuvem não faz sentido. Assim, algumas perguntas devem ser feitas: “Não é possível retirar os dados das instalações por motivos de conformidade?” “A empresa está pronta para priorizar um aplicativo que foi atualizado recentemente?” Assim, a empresa só deve migrar o que faz sentido para a empresa e se não estiver preparada, deve planejar para o futuro.
---------------------------------------------------------------------------------------------------
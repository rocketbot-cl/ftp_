# FTP
  
Conecte e gerencie um servidor FTP  

*Read this in other languages: [English](Manual_ftp_.md), [Português](Manual_ftp_.pr.md), [Español](Manual_ftp_.es.md)*
  
![banner](imgs/Banner_ftp_.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar com FTP
  
Conectar com FTP para gerenciá-lo com Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Servidor|Endereço do servidor FTP|test.ftp.com|
|Porta|Porta do servidor FTP|5518|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|
|Usuário|Usuário do servidor FTP|user@test.com|
|Senha|Senha do usuário do servidor FTP|******|
|TLS|Ativar TLS|True|
|Codificação|Codificação do servidor FTP|utf-8|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|result|

### Listar diretório
  
Lista o diretório do FTP em uma variável do Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Armazenar resultado na variável|Variável onde o resultado será armazenado|Variável|

### Criar diretório
  
Criar diretório no caminho atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do diretório|Nome do diretório a ser criado|test|
|Atribuir resultado a variável|Variável onde o resultado será armazenado|Variável|

### Ir para o diretório
  
Ir para o diretório especificado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do diretório|Nome do diretório para acessar|test|
|Salvar diretório atual na variável|Nome da variável onde o diretório atual será salvo|Variável|

### Carregar arquivo
  
Upload do arquivo para o diretório atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo para carregar|Arquivo que será carregado para o diretório ftp|C:\Users\Usuário\Desktop\test.png|
|Tempo limite|Tempo limite máximo em segundos|10|
|Atribuir resultado à variável|Variável onde o resultado será salvo|Variável|

### Baixar arquivo
  
Baixe o arquivo selecionado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do arquivo para baixar|Nome do arquivo que será baixado do diretório ftp|test.png|
|Caminho para baixar|Caminho onde o arquivo será baixado|C:\Users\Usuário\Desktop|
|Atribuir resultado à variável|Atribui o resultado do download à variável selecionada|Variável|

### Baixar diretório
  
Baixe o diretório atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para baixar|Caminho onde o diretório atual será baixado|C:/Users/Usuário/Desktop|
|Incluir subdiretórios|Se marcado, os subdiretórios serão incluídos no download de forma recursiva|False|
|Atribuir resultado à variável|Atribui o resultado do download à variável selecionada|Variável|

### Apagar arquivo
  
Apagar arquivo no diretório atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do arquivo a apagar|Nome do arquivo que será apagado do diretório atual|test.png|
|Atribuir resultado a variável|Variável onde o resultado da operação será armazenado|Variável|

### Fechar Conexão
  
Fecha a conexão FTP
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

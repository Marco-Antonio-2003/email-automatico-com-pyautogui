Lembre-se de instalar as bibliotecas do código:
Para criar um ambiente virtual em Python, você pode usar o módulo venv. Primeiro, abra um terminal e navegue até o diretório onde deseja criar o ambiente virtual. Em seguida, execute o seguinte comando:

python -m venv nome_do_ambiente

Substitua nome_do_ambiente pelo nome que você deseja dar ao seu ambiente virtual. Isso criará um novo diretório com o nome do ambiente virtual no diretório atual.

Para ativar o ambiente virtual, execute o seguinte comando:

source nome_do_ambiente/bin/activate

Substitua nome_do_ambiente pelo nome do seu ambiente virtual. Quando ativado, você verá o nome do ambiente virtual no prompt do terminal.

Agora você pode instalar as bibliotecas que deseja usar no seu projeto Python usando o comando pip. Certifique-se de que o ambiente virtual esteja ativado antes de executar este comando.

pip install pyautogui
pip install time

Pode substituir o navegador se quiser, mas não recomendo.

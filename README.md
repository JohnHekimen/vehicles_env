# vehicles_env

Análise de veiculos.

Esse app tem como objetivo a criação de histograma e também de gráfico de dispersão em relação ao arquivo vehicles_us.csv


# Observação:
Durante os testes encontrei um comportamento inesperado no Render. Quando adiciono um st.header() ou st.title(), a aplicação funciona normalmente em ambiente local (executando pelo Git Bash). No entanto, após o deploy no Render, o primeiro gráfico é exibido corretamente, mas ao tentar exibir o segundo gráfico, o servidor interrompe a execução da aplicação. Sem o cabeçalho, esse problema não ocorre. Como o código funciona corretamente em ambiente local, acredito que esse comportamento esteja relacionado ao ambiente de hospedagem do Render. Tentei várias formas se solucionar, mas não tive sucesso.


Link da aplicação online no Render:

https://vehicles-env-0kca.onrender.com
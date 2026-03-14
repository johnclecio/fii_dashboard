# 📊 FII Dashboard

Dashboard interativo para acompanhamento de **Fundos Imobiliários (FIIs)**, exibindo informações como preço atual, quantidade de cotas, dividendos e renda mensal estimada.

O projeto utiliza Python para coleta e processamento de dados e um dashboard web interativo utilizando Streamlit.

---

# 🚀 Funcionalidades

* Consulta automática de preços de FIIs
* Cálculo de renda mensal estimada
* Visualização da carteira de FIIs
* Interface web interativa
* Atualização automática dos dados

---

# 🛠 Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* yfinance

---

# 📂 Estrutura do projeto

```
fii_dashboard
│
├── dashboard.py      # Interface web com Streamlit
├── main.py           # Script principal de cálculo da carteira
├── carteira.json     # Dados da carteira de FIIs
├── log.txt           # Logs de execução
└── README.md
```

---

# ⚙️ Instalação

Clone o repositório:

```
git clone https://github.com/seu-usuario/fii_dashboard.git
```

Entre na pasta do projeto:

```
cd fii_dashboard
```

Crie um ambiente virtual:

```
python3 -m venv venv
```

Ative o ambiente virtual:

Mac / Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Instale as dependências:

```
pip install streamlit pandas yfinance
```

---

# ▶️ Executando o projeto

Para rodar o dashboard execute:

```
streamlit run dashboard.py
```

O sistema abrirá automaticamente no navegador:

```
http://localhost:8501
```

---

# 📊 Exemplo de saída

```
Ticker   Preço   Cotas   Dividendo   Renda Mensal
HGLG11   156.83    10      1.10          11.00
MXRF11     9.70   100      0.10          10.00
VGIR11     9.73    80      0.12           9.60
LVBI11   110.55    15      0.75          11.25
XPML11   109.30    12      0.92          11.04

Renda mensal estimada: R$ 52.89
```

---

# 📈 Melhorias futuras

* Gráfico de evolução da renda passiva
* Histórico de dividendos
* Valor total da carteira
* Simulação de reinvestimento de dividendos
* Integração com APIs de mercado

---

# 📄 Licença

Este projeto é open-source e pode ser utilizado para fins de estudo e aprendizado.

---

# 👨‍💻 Autor

Desenvolvido por **John Lima**

Estudante de Engenharia de Software e entusiasta de desenvolvimento backend e análise de dados.

# Previsão da Ibovespa

## 📖 Introdução

Este projeto desenvolve uma estratégia de análise técnica aplicada ao índice **Ibovespa (B3)**, utilizando médias móveis simples (SMA) e exponenciais (EMA) para geração de sinais de compra e venda.  
Além disso, são aplicadas técnicas de **engenharia de atributos**, **normalização de dados**, **tratamento de dados ausentes** e **visualização gráfica** para uma análise mais aprofundada.

O objetivo é simular uma estratégia quantitativa básica de trading e construir uma base sólida para futuros aprimoramentos, como modelagens de séries temporais, deep learning e backtesting avançado.

---

## 🛠 Sobre o Projeto

O projeto está organizado da seguinte forma:

```brash
Previsão da Ibovespa/
├── data/
│   └── ibovespa_data.csv         # Dados históricos baixados via yfinance
├── python/
│   ├── main.py                    # Código principal de execução da estratégia
│   └── visualize_data.py          # Módulo de visualizações gráficas
├── solução.txt                    # Rascunhos e anotações
└── README.md                      # Documentação do projeto
```

- **`main.py`** contém a definição da classe `TradingStrategy`, incluindo:
  - Download de dados históricos;
  - Cálculo de retornos e médias móveis;
  - Geração de sinais de compra e venda;
  - Engenharia de atributos temporais e estatísticos;
  - Tratamento de dados ausentes;
  - Normalização e padronização de dados;
  - Otimização de parâmetros.

- **`visualize_data.py`** é responsável por criar diferentes tipos de gráficos:
  - Evolução do índice;
  - Estratégias de compra e venda;
  - Atributos derivados (rolling means, volatilidade, etc).

---

## 📦 Dependências

Para executar este projeto, é necessário instalar as seguintes bibliotecas Python:

```bash
pip install -r requirements.txt
```
---

Exemplo de requirements.txt:

yfinance
pandas
matplotlib
scikit-learn

Caso prefira instalar manualmente:

```bash
pip install yfinance pandas matplotlib scikit-learn
```

🚀 Como Executar
Clone o repositório:

```bash
git clone <URL-do-repositório>
```

Acesse o diretório do projeto:
```bash
cd caminhoparaodiretorio
```

Execute o script principal:
```bash
python python/main.py
```
---
## 📊 Resultados Esperados
Impressão de estatísticas descritivas no terminal;

Geração de gráficos dinâmicos sobre a evolução dos preços, sinais de trading e atributos estatísticos;

Otimização automática do melhor período de média móvel baseado no retorno acumulado.
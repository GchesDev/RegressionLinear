# Simple Linear Regression Model
## 👀 Overview

Este repositório contém uma implementação simples de um modelo de regressão linear usando a biblioteca Python scikit-learn. O modelo prevê os preços da habitação com base na área da casa.

## 📚 Requeriments
- Python 3.x
- pandas
- scikit-learn
- joblib

## 💻 Usage
1. Clone o repositório
```
git clone https://github.com/GchesDev/LinearRegression
```
2. Navegue até o diretório do Projeto
```
cd nome-do-repositório
```
3. Instale as dependências
```
pip install -r requirements.txt
```
4. Inicie o script
```
python simple_linear_regression.py
```

## 📁 Dataset

O conjunto de dados usado neste exemplo é sintético e consiste em duas colunas:

- area: A área das casas em metros quadrados.
- price: O preço correspondente das casas na moeda local.

## 🗃 Model Training

O modelo é treinado usando as seguintes etapas:

- Importe as bibliotecas necessárias.
- Carregue o conjunto de dados em um DataFrame do pandas.
- Divida o conjunto de dados em conjuntos de treinamento e teste.
- Inicialize um modelo de regressão linear.
- Treine o modelo usando os dados de treinamento.
- Avalie o desempenho do modelo usando o erro quadrático médio (MSE).
- Salve o modelo treinado usando joblib.

## 🔍 Model Evaluation

O desempenho do modelo é avaliado usando a métrica do erro quadrático médio (MSE). Valores mais baixos de MSE indicam melhor desempenho preditivo.

## 📎 Files

- `simple_linear_regression.py`: Python script containing the code for data preprocessing, model training, and evaluation.
- `RegressionLinear.joblib`: Serialized trained model saved for later use.

## ✍ Autor
- [Gches](https://github.com/gchesdev) 

## Licença

[MIT](https://choosealicense.com/licenses/mit/)


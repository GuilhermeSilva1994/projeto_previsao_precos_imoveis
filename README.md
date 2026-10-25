# Previsão de Preços de Imóveis | Machine Learning

Aplicação interativa desenvolvida em **Python e Streamlit** para disponibilizar previsões de preços de imóveis a partir de um modelo de Machine Learning.

🔗 **[Acessar a aplicação](https://projetoprevisaoprecosimoveis.streamlit.app/)**

## Sobre o projeto

Este projeto explora a utilização de técnicas de **Ciência de Dados e Machine Learning** para estimar valores de imóveis com base em características dos dados. O trabalho inclui análise exploratória, preparação das variáveis e disponibilização de um modelo preditivo em uma aplicação web.

> **Contexto dos dados:** o conjunto de variáveis analisado inclui `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income` e `median_house_value`. Confirme a fonte e as condições de uso do dataset antes de publicá-las aqui.

## Objetivo

Construir e disponibilizar uma solução de regressão capaz de estimar o valor mediano de imóveis a partir de atributos demográficos, socioeconômicos e habitacionais.

## Tecnologias

- **Python** — linguagem principal;
- **Pandas e NumPy** — manipulação de dados;
- **Scikit-Learn** — desenvolvimento e utilização de modelos de regressão;
- **Streamlit** — interface interativa e deploy;
- **GeoPandas, Shapely e PyArrow** — tratamento de dados geográficos e arquivos Parquet, quando aplicável;
- **Git e GitHub** — versionamento do projeto.

Consulte o `requirements.txt` para verificar as versões das dependências efetivamente usadas na aplicação.

## Etapas do projeto

1. **Análise exploratória (EDA):** investigação das distribuições, assimetria (`skewness`), curtose (`kurtosis`) e valores extremos.
2. **Preparação dos dados:** tratamento das variáveis utilizadas na modelagem.
3. **Modelagem:** treinamento e avaliação de modelos de regressão.
4. **Aplicação:** integração do modelo treinado a uma interface Streamlit.
5. **Deploy:** publicação da aplicação no Streamlit Community Cloud.

## Modelo e resultados

| Item | Informação |
|---|---|
| Algoritmo final | **[Preencher: ex. Random Forest, XGBoost etc.]** |
| Métrica principal | **[Preencher: MAE, RMSE ou R²]** |
| Resultado no conjunto de teste | **[Preencher com o valor medido]** |
| Estratégia de validação | **[Preencher: holdout, validação cruzada etc.]** |

> Não confunda métricas do treinamento com métricas medidas em dados não vistos. Informe os resultados do conjunto de teste ou validação apropriada.

## Como executar localmente

Recomenda-se utilizar **Python 3.11**, versão do ambiente de desenvolvimento utilizado neste projeto.

```bash
# Clonar o repositório
git clone https://github.com/SEU_USUARIO/projeto_previsao_precos_imoveis.git
cd projeto_previsao_precos_imoveis

# Criar ambiente virtual
python -m venv .venv

# Ativar no Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Instalar dependências
python -m pip install -r requirements.txt

# Executar a aplicação
streamlit run home.py
```

No Linux ou macOS, ative o ambiente virtual com `source .venv/bin/activate`. Substitua `SEU_USUARIO` pelo usuário correto do GitHub.

> Para executar a aplicação, os arquivos de dados e o artefato do modelo precisam estar disponíveis nos caminhos esperados pelo código.

## Estrutura do repositório

O ponto de entrada do aplicativo é o arquivo `home.py`. Consulte as demais pastas do repositório para localizar os módulos Python, dados e artefatos de inferência.

## Próximas melhorias

- [ ] Documentar o algoritmo final e seus hiperparâmetros;
- [ ] Publicar métricas de avaliação e exemplos de previsão;
- [ ] Incluir testes automatizados do pipeline de inferência;
- [ ] Adicionar capturas de tela da aplicação;
- [ ] Descrever limitações do modelo e possíveis fontes de erro.

## Aviso

As previsões são estimativas estatísticas e não substituem uma avaliação imobiliária profissional. A qualidade dos resultados depende dos dados de entrada e das condições em que o modelo foi treinado.

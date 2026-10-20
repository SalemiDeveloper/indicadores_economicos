# Indicadores Econômicos

Pipeline de dados desenvolvido em Python para coletar, validar, transformar e analisar dados da taxa Selic, utilizando a API do Banco Central do Brasil (BCB).

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Engenharia de Dados por meio da construção de um pipeline ETL (*Extract, Transform, Load*).

A aplicação coleta dados econômicos de uma fonte pública, valida sua consistência, transforma os registros para um formato estruturado e gera indicadores que facilitam a análise da variação da taxa Selic.

O projeto utiliza apenas bibliotecas nativas do Python, sem necessidade de banco de dados ou infraestrutura adicional.

## Objetivos

- Consumir dados de uma API pública.
- Implementar etapas de extração, validação e transformação de dados.
- Trabalhar com arquivos JSON e CSV.
- Calcular indicadores a partir de dados históricos.
- Implementar tratamento de erros e testes automatizados.
- Praticar organização de código e boas práticas de desenvolvimento.

## Tecnologias utilizadas

- **Python 3.15**
- API do Banco Central do Brasil
- JSON e CSV
- `unittest` para testes automatizados
- Git e GitHub para versionamento

## Pipeline de dados

O pipeline é composto pelas seguintes etapas:

1. **Extração:** consulta a API do Banco Central e salva os dados brutos em JSON.
2. **Validação:** verifica a estrutura dos registros, datas, valores numéricos, duplicidades e outras inconsistências.
3. **Transformação:** padroniza as datas e exporta os dados validados para CSV.
4. **Geração de indicadores:** calcula a variação da taxa Selic no período e salva os resultados em JSON.

## Estrutura do projeto

```text
indicadores-economicos/
├── data/
│   ├── raw/
│   │   └── selic.json
│   └── processed/
│       ├── selic.csv
│       └── indicators.json
├── src/
│   ├── extract_selic.py
│   ├── validation.py
│   ├── validate_selic.py
│   ├── transform_selic.py
│   ├── generate_indicators.py
│   └── test_validation.py
├── .gitignore
└── README.md
```

## Fonte dos dados

Os dados são obtidos da série 432 do Sistema Gerenciador de Séries Temporais (SGS) do Banco Central do Brasil, referente à meta da taxa Selic.

Documentação e consulta da API:

- [Banco Central do Brasil — SGS](https://www3.bcb.gov.br/sgspub/)
- [API de dados do Banco Central](https://api.bcb.gov.br/)

## Como executar

### Pré-requisitos

- Python instalado.
- Git instalado, caso deseje clonar o repositório.

Não é necessário instalar dependências externas.

### 1. Clonar o repositório

```bash
git clone https://github.com/SalemiDeveloper/indicadores-economicos.git
cd indicadores-economicos
```

### 2. Executar o pipeline

Execute os comandos abaixo, na raiz do projeto, nesta ordem:

```bash
python src/extract_selic.py
python src/validate_selic.py
python src/transform_selic.py
python src/generate_indicators.py
```

Os arquivos gerados serão salvos nos diretórios `data/raw/` e `data/processed/`.

### 3. Executar os testes

```bash
python -m unittest discover -s src -p "test_*.py" -v
```

Os testes verificam cenários como registros válidos, datas futuras, datas duplicadas, valores negativos, valores não numéricos e datas inválidas.

## Exemplo de resultado

Uma execução do pipeline produziu os seguintes indicadores para o período analisado:

```json
{
  "data_inicial": "2026-09-01",
  "data_final": "2026-10-19",
  "selic_inicial": 14.0,
  "selic_final": 13.75,
  "variacao_pontos_percentuais": -0.25,
  "quantidade_observacoes": 49
}
```

Os valores acima representam uma execução específica e podem mudar conforme o período consultado e os dados disponibilizados pela API.

## Próximas melhorias

- Permitir a seleção dinâmica do período de consulta.
- Adicionar outras séries econômicas, como IPCA e câmbio.
- Ampliar a cobertura dos testes automatizados.
- Criar visualizações para facilitar a análise dos indicadores.

## Autor

Desenvolvido por **Pedro Salemi** como projeto de estudo em Python e Engenharia de Dados.
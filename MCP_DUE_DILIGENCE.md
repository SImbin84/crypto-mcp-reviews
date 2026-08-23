# MCP Due Diligence

Run: 2026-08-23T18:25:52Z

| id | verdict | classification | hypothesis_relevance | risk |
| --- | --- | --- | --- | --- |
| coingecko-mcp-server | CANDIDATE_READ_ONLY | READ_ONLY_CANDIDATE | H9_read_only; H7_only_if_historical_funding_confirmed | low |
| mcp-server-ccxt | DEFER | READ_ONLY_CANDIDATE | H9_read_only; H7_only_if_historical_funding_confirmed | medium |
| mcp-server-ccxt-nayshins | DEFER | READ_ONLY_CANDIDATE | H9_read_only; H7_only_if_historical_funding_confirmed | medium |
| cryptominute-news-mcp | CANDIDATE_READ_ONLY | READ_ONLY_CANDIDATE | NEW_NEWS_EVENT_STUDY_NOT_H1-H10 | medium |
| eth-mcp-server | DEFER | READ_ONLY_CANDIDATE | DEFER_EVM_separate_program | medium |
| eth-mcp | DEFER | READ_ONLY_CANDIDATE | DEFER_EVM_separate_program | medium |
| awesome-mcp-servers-finance-crypto | DEFER | MIXED_RISK | H9_read_only; H7_only_if_historical_funding_confirmed | high |

## READ-ONLY candidates

### CoinGecko MCP Server

- URL: https://github.com/cyanheads/coingecko-mcp-server

- Additive value: Добавляет универсальный скриннинг 15k+ монет, историю и метаданные, которых нет в Bitget OHLCV collector.

- H relevance: H9_read_only; H7_only_if_historical_funding_confirmed

- Why not integrate now: Заявлен как read-only data source; write tools отсутствуют. Дальнейшая проверка только на свежесть и документацию.

### CryptoMinute News MCP

- URL: https://github.com/zkoranges/cryptominute-news-mcp

- Additive value: Даёт новостной и Reddit/YouTube сентимент слой для будущих event-study гипотез.

- H relevance: NEW_NEWS_EVENT_STUDY_NOT_H1-H10

- Why not integrate now: Заявлен как read-only data source; write tools отсутствуют. Дальнейшая проверка только на свежесть и документацию.


## Full JSON

- `results/mcp_due_diligence.json`

- `results/mcp_hypothesis_mapping.csv`


> Ни один сервер не разрешён для execution или доступа к секретам без отдельного approval.


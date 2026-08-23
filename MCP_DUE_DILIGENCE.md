# MCP Due Diligence V3

Verified run: 2026-08-23T18:34:06Z

| repo | verified date | latest commit | license | tools verified | write scope | secrets required | classification | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cyanheads/coingecko-mcp-server | 2026-08-23T18:34:06Z | 2026-08-21T15:10:04Z | Apache-2.0 | True | none | none; optional COINGECKO_API_KEY for higher rate limit | READ_ONLY_CANDIDATE | CANDIDATE_READ_ONLY |
| doggybee/mcp-server-ccxt | 2026-08-23T18:34:06Z | 2025-06-03T03:55:44Z | MIT | False | trade/order/transfer/leverage hinted | API key / exchange account | MIXED_RISK | REJECT_FOR_CURRENT_PROGRAM |
| Nayshins/mcp-server-ccxt | 2026-08-23T18:34:06Z | 2025-02-17T18:45:06Z | MIT | False | UNKNOWN | UNKNOWN | UNKNOWN_CAPABILITIES | DEFER |
| zkoranges/cryptominute-news-mcp | 2026-08-23T18:34:06Z | 2026-02-22T13:38:10Z | MIT | True | none | none | READ_ONLY_CANDIDATE | CANDIDATE_READ_ONLY |
| ethpandaops/eth-mcp-server | 2026-08-23T18:34:06Z | 2025-06-24T20:21:35Z | MIT | True | eth_deployContract, eth_callContractMethod, send ETH transactions | private keys / RPC | MIXED_RISK | REJECT |
| 0xKoda/eth-mcp | 2026-08-23T18:34:06Z | 2025-04-01T03:34:38Z | MIT | True | none | RPC key | READ_ONLY_CANDIDATE | DEFER |
| TensorBlock/awesome-mcp-servers | 2026-08-23T18:34:06Z | 2026-08-23T16:49:39Z | MIT | False | N/A | N/A | CATALOG_ONLY | CATALOG_ONLY |

## Source-level evidence

- `results/mcp_source_tool_evidence.csv`

- `results/mcp_source_files.json`

- `results/mcp_cryptominute_sources.json`


## READ-ONLY candidates

### cyanheads/coingecko-mcp-server

- Additive value: Универсальный скриннинг 15k+ монет, метаданные, история, глобальный рынок — нет в Bitget collector.

- H relevance: FUTURE_CROSS_MARKET_RESEARCH

- Why not integrate now: All 8 tools verified read-only from source; schemas confirmed; keyless mode works; no write actions.

### zkoranges/cryptominute-news-mcp

- Additive value: Новостной/сентимент слой + исторические статьи/flash posts/YouTube/Reddit для будущих event-study.

- H relevance: FUTURE_NEWS_EVENT_STUDY

- Why not integrate now: **API_UNRELIABLE**. DNS `api.cryptominute.com` does not resolve from sandbox/network; runtime data access is unconfirmed. No MCP integration until live endpoint reachability is independently verified.

- Repeat rule: do not re-run CryptoMinute probe without a new independent basis: new documented domain, official docs, confirmed endpoint, or infrastructure change.


> Ни один сервер не разрешён для execution или доступа к секретам без отдельного approval.


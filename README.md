# volatility-forecast-research
# Regime-Switching vs GARCH Volatility Forecasting

## Research Question
Do regime-switching volatility models produce statistically superior out-of-sample forecasts compared to standard GARCH models?

This project replicates and extends classical results from:
- Analysis of Financial Time Series – Ruey Tsay
- Time Series Analysis – James Hamilton



## Motivation
Volatility forecasting is central to:
- risk management
- options pricing
- portfolio allocation

Standard GARCH models assume one volatility regime.  
But markets exhibit structural breaks and crisis regimes.

We test whether regime-switching models capture this better.



## Background

Key concepts:
- ARCH/GARCH models
- Hidden Markov models
- Volatility clustering
- Heavy-tailed returns

Primary references:
- Analysis of Financial Time Series – Tsay
- Time Series Analysis – Hamilton
- Relevant papers from arXiv quantitative finance



## Methodology

### Data
Assets studied:
- SPY (equity index proxy)
- BTC-USD (crypto)

Sources:
- Yahoo Finance
- Binance API

We compute:
- log returns
- realized volatility (rolling window)



### Models
Baseline:
- GARCH(1,1)
- EGARCH
- GJR-GARCH

Research model:
- Markov-switching volatility model
- Hidden Markov Model regime detection



### Evaluation Metrics
- Mean Squared Error
- QLIKE loss
- Diebold-Mariano test
- Crisis-period performance

Out-of-sample period: 2021–2025



## Results (To Be Updated)

Example plots:
- predicted vs realized volatility
- regime probability over time
- model comparison table

(Add figures here later)

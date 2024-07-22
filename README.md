# Binary-Options-A.I.-with-Streaming-Data

Este projeto trata-se de um modelo de I.A. para tentar fazer previsões de opções binárias, definindo a próxima ordem como compra ou venda, no período estipulado.

Para realizar este projeto fiz a extração das candles dos últimos anos e fiz um grande tratamento de dados. Deixei apenas as colunas que eu iria utilizar e criei uma nova, indicando se a próxima vela seria de compra ou venda (coluna target).

Para implantação do modelo de I.A., optei por utilizar redes neurais, mais especificamente LSTM (Long Short-Term Memory) já que estamos falando de uma grande quantidade de dados e fatores passados que precisam ser reconsiderados nas futuras previsões.

Além disso, o modelo utiliza extração dos dados em streaming das velas da plataforma IQOption.

(Note que o modelo pode ser treinado durante mais tempo, alterando o número de gerações e, após isso, pode ser extraído para um arquivo, como fiz no código)

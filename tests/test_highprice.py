
def test_high_price_variable():
    assert 'HighPrice' in df.columns, "La columna 'HighPrice' no fue creada en el DataFrame"
    assert df['HighPrice'].isin([0, 1]).all(), "'HighPrice' debe contener solo valores binarios (0 o 1)"

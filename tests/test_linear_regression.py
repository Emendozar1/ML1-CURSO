
def test_linear_regression_training():
    from sklearn.linear_model import LinearRegression
    assert 'lr' in globals(), "No se encontró el modelo 'lr'"
    assert isinstance(lr, LinearRegression), "'lr' no es una instancia de LinearRegression"
    assert hasattr(lr, 'coef_'), "El modelo 'lr' no ha sido entrenado correctamente"

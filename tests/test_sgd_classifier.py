
def test_sgd_classifier_training():
    from sklearn.linear_model import SGDClassifier
    assert 'sgd_cls' in globals(), "No se encontró el modelo 'sgd_cls'"
    assert isinstance(sgd_cls, SGDClassifier), "'sgd_cls' no es una instancia de SGDClassifier"
    assert hasattr(sgd_cls, 'coef_'), "El modelo 'sgd_cls' no ha sido entrenado correctamente"

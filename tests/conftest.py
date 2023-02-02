import pytest


@pytest.fixture()
def system_intering():
    print('Вход в систему выполнен')
    yield  # переход на функцию
    print('Выход из системы')

@pytest.fixture(scope='module')
def some():
    print('Начало')
    yield #переход на на тест(файл)
    print('Конец')
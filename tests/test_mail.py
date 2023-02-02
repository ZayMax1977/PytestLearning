import pytest

@pytest.fixture()
def system_intering():
    print('Вход в систему выполнен')
    yield
    print('Выход из системы')

def test_send_mail_1(system_intering):
    print('Письмо 1 отправлено')

def test_send_mail_2(system_intering):
    print('Письмо 2 отправлено')

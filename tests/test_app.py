from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html_deve_retornar_ok_e_ola_mundo_em_html(client):
    response = client.get('/texto')

    assert response.status_code == HTTPStatus.OK
    assert '<p>olá mundo</p>' in response.text


def test_create_user_deve_retornar_201_e_user_criado_com_nome_e_email(client):
    usuario_a_ser_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }
    usuario_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
    }

    response = client.post('/users/', json=usuario_a_ser_criado)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == usuario_criado


def test_get_users_deve_retornar_ok_e_lista_de_usuarios(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Julia',
                'email': 'ju.araujo11@yahoo.com.br',
            }
        ]
    }


def test_update_user_deve_retornar_not_found_se_nao_tiver_user(client):
    usuario_a_ser_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/10', json=usuario_a_ser_alterado)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_deve_retornar_not_found_se_nao_tiver_id(client):
    usuario_a_ser_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/0', json=usuario_a_ser_alterado)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_deve_retornar_ok_se_nao_tiver_user(client):
    usuario_a_ser_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/1', json=usuario_a_ser_alterado)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
    }


def test_delete_user_deve_retornar_not_found_se_nao_tiver_user(client):
    response = client.delete('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_not_found_se_nao_tiver_id(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_ok_se_tiver_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_get_user_deve_retornar_not_found_se_nao_tiver_user(client):
    response = client.get('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_deve_retornar_not_found_se_nao_tiver_id(client):
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_deve_retornar_ok_se_tiver_user(client):
    usuario_a_ser_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }
    usuario_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
    }

    response = client.post('/users/', json=usuario_a_ser_criado)
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == usuario_criado

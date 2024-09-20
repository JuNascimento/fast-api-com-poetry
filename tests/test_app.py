from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_html_deve_retornar_ok_e_ola_mundo_em_html(client):
    response = client.get('/texto')

    assert response.status_code == HTTPStatus.OK
    assert '<p>olá mundo</p>' in response.text


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user_deve_retornar_201_e_user_criado_com_nome_e_email(
    client, user
):
    usuario_a_ser_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }
    usuario_criado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'id': 2,
    }

    response = client.post('/users/', json=usuario_a_ser_criado)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == usuario_criado


def test_create_user_deve_retornar_404_e_mensagem_de_erro_se_usuario_existir(
    client, user
):
    usuario_a_ser_criado = {
        'username': 'Teste',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }
    response = client.post('/users/', json=usuario_a_ser_criado)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_deve_retornar_404_e_mensagem_de_erro_se_email_existir(
    client, user
):
    usuario_a_ser_criado = {
        'username': 'Julia',
        'email': 'teste@test.com',
        'password': '1234globo',
    }
    response = client.post('/users/', json=usuario_a_ser_criado)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists'}


def test_get_users_deve_retornar_ok_e_lista_de_usuarios_vazia(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_get_users_deve_retornar_ok_e_lista_de_usuarios(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user_deve_retornar_not_found_se_nao_tiver_user(client, user):
    usuario_a_ser_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/10', json=usuario_a_ser_alterado)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_deve_retornar_not_found_se_nao_tiver_id(client, user):
    usuario_a_ser_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/0', json=usuario_a_ser_alterado)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_deve_retornar_ok_se_tiver_user(client, user):
    usuario_alterado = {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'password': '1234globo',
    }

    response = client.put('/users/1', json=usuario_alterado)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Julia',
        'email': 'ju.araujo11@yahoo.com.br',
        'id': 1,
    }


def test_delete_user_deve_retornar_not_found_se_nao_tiver_user(client, user):
    response = client.delete('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_not_found_se_nao_tiver_id(client, user):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_ok_se_tiver_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_get_user_deve_retornar_not_found_se_nao_tiver_user(client, user):
    response = client.get('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_deve_retornar_not_found_se_nao_tiver_id(client, user):
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_deve_retornar_ok_se_tiver_user(client, user):
    usuario_criado = {'username': 'Teste', 'email': 'teste@test.com', 'id': 1}

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == usuario_criado

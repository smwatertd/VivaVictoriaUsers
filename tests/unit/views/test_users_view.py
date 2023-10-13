from unittest.mock import MagicMock

from exceptions import UserAlreadyExists

import pytest

from schemas import CreateUserSchema

from tests.test_case import TestCase


class TestUsersView(TestCase):
    def test_register_success_response(
        self,
        session: MagicMock,
        create_user_schema: CreateUserSchema,
        create_user_service: MagicMock,
    ) -> None:
        response = self.client.post('/users', json=create_user_schema.model_dump())

        assert 201 == response.status_code
        assert response.json is None
        create_user_service.assert_called_once_with(session, create_user_schema)

    def test_register_blank_email(
        self,
        create_user_schema: CreateUserSchema,
    ) -> None:
        response = self.client.post('/users', json=create_user_schema.model_dump(exclude=['email']))

        assert 400 == response.status_code
        assert {'status': 'error', 'message': 'email is required'} == response.json, response.json

    def test_register_blank_username(
        self,
        create_user_schema: CreateUserSchema,
    ) -> None:
        response = self.client.post('/users', json=create_user_schema.model_dump(exclude=['username']))

        assert 400 == response.status_code
        assert {'status': 'error', 'message': 'username is required'} == response.json, response.json

    def test_register_blank_password(
        self,
        create_user_schema: CreateUserSchema,
    ) -> None:
        response = self.client.post('/users', json=create_user_schema.model_dump(exclude=['password']))

        assert 400 == response.status_code
        assert {'status': 'error', 'message': 'password is required'} == response.json, response.json

    @pytest.mark.usefixtures('session')
    def test_register_user_already_exists(
        self,
        create_user_service: MagicMock,
        create_user_schema: CreateUserSchema,
    ) -> None:
        create_user_service.side_effect = UserAlreadyExists('user already exists')

        response = self.client.post('/users', json=create_user_schema.model_dump())

        assert 400 == response.status_code
        assert {'status': 'error', 'message': 'user already exists'} == response.json, response.json

#!/usr/bin/env python3
"""Session authentication module for the API.
"""
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session authentication class."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id."""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        if request is None:
            return None
        '''Step 1: Retrieve session cookie (_my_session_id)'''
        session_cookie = self.session_cookie(request)
        if not session_cookie:
            return None
        '''Step 2: Get User ID based on session ID'''
        user_id = self.user_id_for_session_id(session_cookie)
        if not user_id:
            return None
        '''Step 3: Retrieve User instance from database'''
        user_instance = User.get(user_id)
        return user_instance

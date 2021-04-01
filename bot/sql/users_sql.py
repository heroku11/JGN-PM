#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" users Table """

from sqlalchemy import (
    Column,
    String,
    Integer
)
from . import (
    SESSION,
    BASE
)


class Users(BASE):
    """ Daftar Pesan Tersimpan Pengguna """
    __tablename__ = "Pengguna"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14))
    um_id = Column(Integer)
    mu_id = Column(Integer)
    kopp_id = Column(Integer)

    def __init__(self, message_id, chat_id, um_id, mu_id, kopp_id):
        self.message_id = message_id
        self.chat_id = str(chat_id)  # ensure string
        self.um_id = um_id
        self.mu_id = mu_id
        self.kopp_id = kopp_id

    def __repr__(self):
        return "<User %s>" % self.chat_id


Users.__table__.create(checkfirst=True)


def add_user_to_db(
    message_id: int,
    chat_id: int,
    um_id: int,
    mu_id: int,
    kopp_id: int
):
    """ Tambahkan Pesan Pengguna di Daftar """
    __user = Users(message_id, str(chat_id), um_id, mu_id, kopp_id)
    SESSION.add(__user)
    SESSION.commit()


def get_user_id(message_id: int):
    """ Dapatkan Id_Pengguna Dari Id_Pesan """
    try:
        s__ = SESSION.query(Users).get(str(message_id))
        if s__:
            return int(s__.chat_id), s__.um_id
        return None, None
    finally:
        SESSION.close()


def get_chek_dmid(um_id: int):
    """ Dapatkan Daftar Id_pengguna yang Dihapus"""
    try:
        all_lst = SESSION.query(
            Users
        ).filter(
            Users.um_id == um_id
        ).all()
        if all_lst:
            return all_lst[-1]
    finally:
        SESSION.close()


def get_chek_mdid(kopp_id: int):
    """ Dapatkan Daftar Id_pengguna yang Dihapus dari kopp_id """
    try:
        all_lst = SESSION.query(
            Users
        ).filter(
            Users.kopp_id == kopp_id
        ).all()
        if all_lst:
            return all_lst[-1]
    finally:
        SESSION.close()

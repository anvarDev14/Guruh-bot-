from aiogram import Dispatcher
from . import admins
from . import group_chat
from . import private_chat
from .admins import AdminFilter
from .group_chat import IsGroup
from .private_chat import IsPrivate

from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)


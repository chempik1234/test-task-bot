from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    login = State()
    choose_surface = State()
    choose_channel = State()

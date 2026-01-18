from aiogram.filters import CommandStart, Command
from aiogram import F, types
from aiogram.types import Message, CallbackQuery
from aiogram import Router
import apps.keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database import conn,cur
import datetime
router = Router()

class Form(StatesGroup):
    waiting_for_result = State()
    

avalible_number = [1,2,3,4,5,6,7,8,9,10]
waiting_for_player_id = 0

@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer("Привет нажми на кнопку!", reply_markup=kb.main_menu())
    

@router.callback_query(F.data == "timing")
async def timing_coach(callback: CallbackQuery):
    if waiting_for_player_id >= 0:
        await callback.answer("")
        await callback.message.edit_text("Теперь выбери роль", reply_markup=kb.choice_role())
    elif waiting_for_player_id == 0:
        @router.message_handler(commands=['set_player_id'])
        async def set_player_id(message: types.Message):
                await message.answer("Сначало введите ваш Steam32 ID:")
                await Form.waiting_for_player_id.set()
    

@router.callback_query(F.data == "tilt")
async def timing_coach(callback: CallbackQuery):
        await callback.answer("")
        await callback.message.edit_text("Когда закончишь катку,\n\nвыбери исход игры:", reply_markup=kb.tilt_menu())

@router.callback_query(F.data == "back_to_main_menu")
async def timing_coach(callback: CallbackQuery):
        await callback.answer("")
        await callback.message.edit_text("Привет нажми на кнопку!", reply_markup=kb.main_menu())

@router.callback_query(F.data == "win")
async def timing_coach(callback: CallbackQuery, state: FSMContext):
        await callback.answer("Записано!")
        await callback.message.answer("Нажми на кнопку!", reply_markup=kb.main_menu())
        await state.set_state(Form.waiting_for_result)

@router.callback_query(F.data =="lose")
async def invalid_anger_level(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Насколько ты зол из за этой катки по шкале от 1 до 10?")


@router.message()
async def final(message: Message, state: FSMContext):
      user_data = await state.get_data()
      await message.answer(f"Вы выбрали {message.text} и {user_data[waiting_for_player_id]}")
      
import asyncio
from datetime import datetime

from telethon.errors import BadRequestError, FloodWaitError, ForbiddenError

from userbot import jmthon

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id, time_formatter
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import check_is_black_list, get_all_bl_users
from ..sql_helper.bot_starters import del_starter_from_db, get_all_starters
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from .botmanagers import (
    ban_user_from_bot,
    get_user_and_reason,
    progress_str,
    unban_user_from_bot,
)

LOGS = logging.getLogger(__name__)

plugin_category = "bot"
botusername = Config.TG_BOT_USERNAME
cmhd = Config.COMMAND_HAND_LER


@jmthon.bot_cmd(
    pattern=f"^bot$",
    from_users=Config.OWNER_ID,
)
async def bot_help(event):
    await event.reply(
        f"test bot :) ",
        link_preview=False,
    )


@jmthon.ar_cmd(
    pattern=f"^التكرار (تفعيل|تعطيل)$",
    command=("التكرار", plugin_category),
    info={
        "header": "تشغيل وايقاف التكرار في البوت الخاص بك",
        "description": " عند التشغيل يحظر المزعجين تلقائيًا الذين يكررون 10 رسائل او يعدلون 10 تعديلات في وقت واحد.",
        "usage": [
            "التكرار تفعيل",
            "التكرار تعطيل",
        ],
    },
)
async def ban_antiflood(event):
    "To enable or disable bot antiflood."
    input_str = event.pattern_match.group(1)
    if input_str == "تفعيل":
        if gvarstatus("bot_antif") is not None:
            return await edit_delete(event, "**▾∮ بالفعل تم تفعيل تحذير التكرار  ✅**")
        addgvar("bot_antif", True)
        await edit_delete(event, "`**▾∮ تم تفعيل تحذير التكرار  ☑️**")
    elif input_str == "تعطيل":
        if gvarstatus("bot_antif") is None:
            return await edit_delete(event, "**▾∮ بالفعل تم تعطيل تحذير التكرار ❌**")
        delgvar("bot_antif")
        await edit_delete(event, "**▾∮ تم تعطيل تحذير التكرار ✘**")

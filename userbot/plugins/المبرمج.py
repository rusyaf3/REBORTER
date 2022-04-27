import random
import re
import time

from telethon.events import CallbackQuery

from userbot import StartTime, jmthon

from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="المبرمج$",
    command=("المبرمج", plugin_category),
    info={
        "header": "لأظهار مبرمج السورس",
        "usage": [
            "{tr}المبرمج",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    gvarstatus("ALIVE_EMOJI") or "  - "
    gvarstatus("ALIVE_TEXT")
    CAT_IMG = (
        gvarstatus("ALIVE_PIC") or " https://telegra.ph/file/5715569276b4b8e051c7c.jpg "
    )
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f" 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙍𝙀𝘽𝙊𝙍𝙏𝙀𝙍\n"
        cat_caption += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        cat_caption += f"🧑‍💻╖ مبرمج السورس  : @E_l_k_e_a_t_i_b\n"
        cat_caption += f"🌐╢ قناة السورس :  @RBBOU\n"
        cat_caption += f"💌╜ جروب الدعم : @Music54Elkeatib\n"
        cat_caption += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )


@jmthon.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)

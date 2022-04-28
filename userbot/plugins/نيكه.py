import asyncio

from userbot import CMD_HELP, jmthon
from userbot.utils import admin_cmd

#
@jmthon.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "اشتمه":

        await event.edit(input_str)

        animation_chars = [
            "كسمك 💞 `",
            "يعرص 💞 `",
            "يمتناك 💞 `",
            "هنيكك 💞 `",
            "خد يكسمك 💞 `",
            "هنيك شعب اللي جابتك 💞 `",
            "يبن لبن زبي 💞 `",
            "كسم عيلتك💞 `",
            "كسم خالك 💞 `",
            "كسم خالتك 💞 `",
            "كسم عمك 💞 `",
            "كسم عمتك 💞 `",
            "كسم امك 💞 `",
            "كسم ابوك 💞 `",
            "كسم اختك 💞 `",
            "كسمك لاجل سيزر 💞 `",
            "كسمك لاجل شادو 💞 `",
            "كسمك لاجل عسليه 💞 `",
            "كسم لاجل الخطيب 💞 `",
            "كسمك لاجلي 💞 `",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])


CMD_HELP.update({"اشتمه": ".اشتمه \nفقط ارسل الامر "})


#لا تسرق الفكره يكسمك
#تعديل المطور سيزر
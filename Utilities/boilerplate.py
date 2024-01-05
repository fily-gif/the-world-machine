from interactions import *
from Utilities.fancysend import *
import Utilities.badge_manager as badge_manager
from Utilities.bot_icons import *


class Command(Extension):

    @slash_command(description="This is a Boilerplate Command.")
    @slash_option(name="option_name", description="This is a Boilerplate Option.", opt_type=OptionType.STRING)
    async def hello(self, ctx: SlashContext, option_name: str):
        await fancy_message(ctx, "Hello, " + option_name)

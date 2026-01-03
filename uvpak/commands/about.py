import uvicore
from uvicore.support.dumper import dump, dd
from uvicore.exceptions import SmartException
from uvicore.console import command, argument, option


# Get running app name and version
app_name = uvicore.app.name
app_version = uvicore.app.package(main=True).version

@command()
async def cli():
    """Welcome to Uvpak!"""
    try:

        print(f"""Welcome to Uvpak v{app_version}, the Unix Variant Package Manager!

Uvpak is a modern package manager for all Unix-like operating systems, built with Python!
A universal package manager for Linux, MacOS, BSD, WSL, Cygwin and more!

By default, Uvpak comes with NO pre installed package registries.  You must build and add
your own package registries that contain the software that YOU want to distribute and
install for your own systems and use cases.  This is YOUR package manager to distriute
YOUR artifacts the way YOU want to!

To get started, please refer to the Uvpak documentation at https://uvpak.mreschke.com""")

    except SmartException as e:
        # Python exit() with any value means "error" in bash exit code speak!
        exit(e.detail)



# --------------------------------------------------------------------------
# Example: Command with arguments and options
# --------------------------------------------------------------------------
# @command(help="This is another place to set command help messages")
# @argument('id_or_name')
# @option('--tenant', help='Tenant')
# @option('--coin', default='BTC', help='Coin with Default')
# @option('--json', is_flag=True, help='Output results as JSON')
# async def get(id_or_name: str, tenant: str, coin: str, json: bool):
#     """This shows up as the commands help message"""
#     # ex: ./uvicore cmdname namearg --tenant bob --json
#     try:
#         # Do stuff
#         pass
#     except SmartException as e:
#         # Python exit() with any value means "error" in bash exit code speak!
#         exit(e.detail)

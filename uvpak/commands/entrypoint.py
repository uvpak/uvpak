import os
import sys
import uvicore
from uvpak.package import bootstrap
from uvicore.support.module import load
from uvicore.console import click, group

# Bootstrap the Uvicore application from the console entrypoint
app = bootstrap.Application(is_console=True)()

# Get running app name and version
app_name = uvicore.app.name
app_version = uvicore.app.package(main=True).version

# Define a new asyncclick group
@group(help=f"""
    \b
    {app_name} v{app_version}
    To get started, please refer to the Uvpak documentation at https://uvpak.mreschke.com
""")
@click.pass_context
async def cli(ctx):
    # Console startup event dispatcher
    await uvicore.ioc.make('uvicore.console.events.command.Startup')().codispatch()

    # Console shutdown even dispatcher
    ctx.call_on_close(uvicore.ioc.make('uvicore.console.events.command.Shutdown')().codispatch)

# Dynamically add in all commands from this package matching this command_group
command_group='uvpak'
package = uvicore.app.package(main=True);
if 'console' in package:
    if (package.registers.commands and uvicore.app.is_console):
        for key, group in package.console['groups'].items():
            if key == command_group:
                for command_name, command_class in group.commands.items():
                    cli.add_command(load(command_class).object, command_name)

# Instantiate the asyncclick group
try:
    cli(_anyio_backend='asyncio')
except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

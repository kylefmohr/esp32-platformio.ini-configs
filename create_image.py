# The purpose of this script is to create a self-contained firmware image file that can be flashed directly with esptool.py at address 0x0
#
# This can be easily added to your PlatformIO project by adding the following to your `platformio.ini` file:
# extra_scripts = create_image.py
Import("env")


board = env.GetProjectOption("board")
environment = env.subst("$PIOENV")
program_path = env.subst("$PROG_PATH")
program_root = "/".join(program_path.split("/")[:program_path.split("/").index(".pio")])
home_directory = program_path.split("/")[2]
home_directory = "/home/" + home_directory

build_commands = []

bootloader_offset = "0x0000 "
# esptool_board = "esp32s3"
if "s3" in board:
    esptool_board = "esp32s3"
elif "s2" in board:
    esptool_board = "esp32s2"
elif "c3" in board:
    esptool_board = "esp32c3"
elif "c6" in board:
    esptool_board = "esp32c6"
elif "h2" in board:
    esptool_board = "esp32h2"
elif "c5" in board:
    esptool_board = "esp32c5"
    bootloader_offset = "0x2000 "
elif "esp32" in board:
    esptool_board = "esp32"
    bootloader_offset = "0x1000 "
else:
    raise ValueError("Couldn't determine board type for the esptool.py command")
build_commands.append("pio run -e " + environment)
build_commands.append("/usr/bin/python3 " + home_directory + "/.platformio/packages/tool-esptoolpy/esptool.py --chip " + esptool_board + " merge_bin " + \
    bootloader_offset + program_root + "/.pio/build/" + environment + "/bootloader.bin \
    0x8000 " + program_root + "/.pio/build/" + environment + "/partitions.bin \
    0xe000 " + home_directory + "/.platformio/packages/framework-arduinoespressif32/tools/partitions/boot_app0.bin \
    0x10000 " + program_root + "/.pio/build/" + environment + "/firmware.bin -o " + program_root + "/" + environment + "_image.bin")

env.AddCustomTarget(
    name="CreateImage",
    dependencies=None,
    actions=build_commands,
    
    title="Create Image",
    description="Generate images for each board, ready to flash with esptool.py at 0x0",
)

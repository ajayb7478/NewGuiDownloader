@echo off
pyinstaller --onefile --windowed --icon="icon.ico" --add-data "icon.ico;." --add-data "button_1.png;." --add-data "image_1.png;." --add-data "image_2.png;." gui.pyw


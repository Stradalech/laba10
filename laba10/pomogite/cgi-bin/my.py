#! /usr/bin/python3
import sys
# решение проблемы с отображением кириллицы
sys.stdout.buffer.write(b'Content-type: text/html;charset=utf-8\n\n')

print("Привет мир")
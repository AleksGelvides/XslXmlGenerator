from lxml import etree
import os

# Определяем путь к директории, в которой находится скрипт
dir_path = os.path.dirname(os.path.abspath(__file__))
res_path = os.path.join(dir_path, 'res')

# Получаем список файлов в текущей директории
files = os.listdir(res_path)

# Находим xml и xsl файлы
xml_file = None
xsl_file = None
for file in files:
    if file.endswith(".xml"):
        xml_file = os.path.join(res_path, file)
    elif file.endswith(".xsl"):
        xsl_file = os.path.join(res_path, file)

# Если не удалось найти xml или xsl файл, выводим соответствующее сообщение
if xml_file is None or xsl_file is None:
    print("Не удалось найти xml или xsl файл.")
else:
    # Открываем xml и xsl файлы
    xml_file = etree.parse(xml_file)
    xsl_file = etree.parse(xsl_file)

    # Создаем XSLT процессор и применяем XSLT преобразование к XML
    transform = etree.XSLT(xsl_file)
    result = transform(xml_file)

    # Записываем результат в файл
    result_file = os.path.join(dir_path, "result.html")
    with open(result_file, "wb") as f:
        f.write(result)
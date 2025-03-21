import os
import sys

sys.path.insert(0, os.path.abspath('../../sbi_special_docx_master'))

def get_version():
    with open("../../sbi_special_docx_master/__init__.py", "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"\'')
    raise RuntimeError("Unable to find version string.")

project = 'sbi_special_docx_master'
copyright = '2025, TheDaniell'
author = 'TheDaniell'
release = get_version()

extensions = []

# Можливість використання розмітки - "Google-style docstrings"
extensions.append('sphinx.ext.napoleon')
napoleon_include_private_with_doc = True
napoleon_include_private = True

# Додає до сторінок документації посилання, за допомогою яких можна переглянути первинний код.
extensions.append('sphinx.ext.viewcode')

# Дозволяє автоматично генерувати документацію з докстрінгів та анотацій коду
extensions.append('sphinx.ext.autodoc')
# autodoc_dumb_docstring = True  # Дозволяє генерувати документацію для об'єктів, які не мають докстрінгів.
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True
}

autodoc_typehints = 'description'

# Спрощує генерацію автоматичних зведених звітів для класів та функцій
extensions.append('sphinx.ext.autosummary')
autosummary_generate = True  # дозволяє автоматично генерувати зведені звіти

# Кнопка copy у фрагментах коду:
extensions.append('sphinx_copybutton')

# Кнопка вимкнення виводу у фрагментах коду:
extensions.append('sphinx_toggleprompt')
toggleprompt_offset_right = 35

# Зміст модулів та класів (заміна аутосаммарі)
# - автоматично збирає інформацію про класи, функції та методи, що містяться в цьому модулі
extensions.append('sphinx_automodapi.automodapi')
# - допомагає коректно розрізняти об'єкти з однаковими іменами, такі як методи класу та функції
# extensions.append('sphinx_automodapi.smart_resolver')
# - чи слід показувати члени класу в документації:
numpydoc_show_class_members = False

# Налаштування пошуку
# extensions.append('sphinx_search.extension')
# html_search_language = 'ru'


todo_include_todos = True
source_suffix = ['.rst']
master_doc = 'index'
add_function_parentheses = True
add_module_names = True

templates_path = ['_templates']
exclude_patterns = []

language = 'uk_UA'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'style_nav_header_background': '#2980B9',
    'logo_only': False,
    'display_version': True,
}
html_show_copyright = True
html_show_sphinx = False
html_show_sourcelink = False
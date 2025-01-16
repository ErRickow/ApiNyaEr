import os
import sys

# Tambahkan jalur ke modul proyek utama
sys.path.insert(0, os.path.abspath("./ApiNyaEr"))

# Informasi proyek
project = "ApiNyaEr"
copyright = "2025, ErNewDev0"
author = "ErRickow"
release = "1.4"

# -- Konfigurasi Umum -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",  # Menunjukkan waktu kompilasi
    "sphinx.ext.doctest",  # Menyertakan pengujian dokumentasi
    "sphinx.ext.autodoc",  # Mendokumentasikan kode secara otomatis
    "sphinx.ext.autosummary",  # Membuat ringkasan otomatis
    "sphinx.ext.intersphinx",  # Menghubungkan dengan dokumentasi eksternal
    "sphinx.ext.napoleon",  # Mendukung Google-style docstrings
    "sphinx_autodoc_typehints",  # Menambahkan tipe anotasi Python
    "sphinx.ext.viewcode",  # Menyertakan tautan ke kode sumber
]

# Gunakan mode gelap secara default jika tema mendukung
default_dark_mode = True

# Direktori template
templates_path = ["_templates"]

# Pola file yang akan diabaikan
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Mesin LaTeX untuk menghasilkan PDF
latex_engine = "xelatex"

# -- Konfigurasi Output HTML -----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Tema HTML
html_theme = "sphinx_rtd_theme"

# Direktori file statis
html_static = ["_static"]

# Logo proyek
html_logo = "logo.png"

# Opsi tambahan untuk HTML
html_show_sphinx = False  # Sembunyikan tautan "Built with Sphinx"
html_show_copyright = False  # Sembunyikan teks hak cipta default

# Autosectionlabel (untuk referensi antar dokumen)
autosectionlabel_prefix_document = True

# Hoverxref (munculan referensi)
hoverxref_auto_ref = True
hoverxref_roles = ["term"]

# -- Pengaturan Dokumentasi Otomatis ---------------------------------------

# Atur autodoc untuk mendokumentasikan semua anggota secara default
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "show-inheritance": True,
}
autosummary_generate = True  # Membuat ringkasan otomatis

# Konfigurasi untuk intersphinx (tautan ke dokumentasi eksternal)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

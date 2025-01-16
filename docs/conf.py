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
extensions = [
    "sphinx.ext.duration",         # Menunjukkan waktu kompilasi
    "sphinx.ext.doctest",          # Menyertakan pengujian dokumentasi
    "sphinx.ext.autodoc",          # Mendokumentasikan kode secara otomatis
    "sphinx.ext.autosummary",      # Membuat ringkasan otomatis
    "sphinx.ext.intersphinx",      # Menghubungkan dengan dokumentasi eksternal
    "sphinx.ext.napoleon",         # Mendukung Google-style docstrings
    "sphinx_autodoc_typehints",    # Menambahkan tipe anotasi Python
    "sphinx.ext.viewcode",         # Menyertakan tautan ke kode sumber
]

# Pola file yang akan diabaikan
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Mesin LaTeX untuk menghasilkan PDF
latex_engine = "xelatex"

# -- Konfigurasi Output HTML -----------------------------------------------
# Tema HTML
html_theme = "sphinx_rtd_theme"

# Logo proyek (opsional, bisa dihapus jika tidak digunakan)
html_logo = None

# Opsi tambahan untuk HTML
html_show_sphinx = False            # Sembunyikan tautan "Built with Sphinx"
html_show_copyright = False         # Sembunyikan teks hak cipta default

# Autosectionlabel (untuk referensi antar dokumen)
autosectionlabel_prefix_document = True

# Hoverxref (munculan referensi)
hoverxref_auto_ref = True
hoverxref_roles = ["term"]

# -- Pengaturan Dokumentasi Otomatis ---------------------------------------
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": False,
    "show-inheritance": True,
}
autosummary_generate = True  # Membuat ringkasan otomatis
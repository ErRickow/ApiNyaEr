import asyncio
import inspect
import json

import aiofiles

from ApiNyaEr import apinya


# Fungsi pembantu untuk menguji setiap metode AI
async def test_method(method, *args):
    try:
        if inspect.iscoroutinefunction(method):
            result = await method(*args)  # Jika asinkron, tunggu hasilnya
        else:
            result = method(*args)  # Jika sinkron, panggil langsung
        status = "✅"  # Tandai berhasil
        return status, result
    except Exception as e:
        status = "❌"  # Tandai gagal
        return status, str(e)


# Memformat docstring menjadi format markdown yang lebih mudah dibaca
# untuk README
def format_docstring(docstring):
    lines = docstring.splitlines()
    formatted_lines = []
    in_section = False
    nested_item = False

    for line in lines:
        stripped_line = line.strip()

        # Periksa apakah itu header bagian seperti "Args:", "Returns:",
        # "Raises:"
        if stripped_line in ["Args:", "Returns:", "Raises:"]:
            formatted_lines.append(f"**{stripped_line}**")
            in_section = True
            nested_item = False
        # Menangani baris yang terindented
        elif in_section and line.startswith("    "):
            # Deteksi item bersarang dalam bagian
            if stripped_line.startswith("- "):
                formatted_lines.append(f"    - {stripped_line[2:]}")
                nested_item = True
            else:
                parts = stripped_line.split(": ", 1)
                if len(parts) == 2 and not nested_item:
                    formatted_lines.append(f"  - **{parts[0]}**: {parts[1]}")
                else:
                    formatted_lines.append(f"    {stripped_line}")
        elif stripped_line == "":
            formatted_lines.append("")  # Menjaga baris kosong
            in_section = False
            nested_item = False
        else:
            # Baris deskripsi umum di luar bagian
            if formatted_lines and formatted_lines[-1].startswith("**Description**"):
                formatted_lines[-1] += f" {stripped_line}"
            else:
                formatted_lines.append(f"**Deskripsi**:\n{stripped_line}")
            in_section = False
            nested_item = False

    return "\n".join(formatted_lines)


def format_result(result):
    if isinstance(result, dict):
        json_content = json.dumps(result, indent=4)
        return f"```json\n{json_content}\n```"
    elif isinstance(result, list):
        if len(result) > 0 and isinstance(result[0], dict):
            json_content = json.dumps(result, indent=4)
            return f"```json\n{json_content}\n```"
        else:
            return "```text\n" + "\n".join(map(str, result)) + "\n```"
    else:
        return f"```text\n{str(result)}\n```"


# Fungsi utama untuk menghasilkan status AI dan dokumentasi fungsinya


async def generate_ai_status(methods):
    function_statuses = []
    readme_content = []
    status_content = []
    function_count = 1

    for name, method in methods:
        if name.startswith("_"):
            continue  # Lewati metode privat

        signature = inspect.signature(method)
        docstring = inspect.getdoc(method) or "Tidak ada deskripsi yang tersedia."
        formatted_name = name.replace("_", "-").lower()

        # Membuat entri status dengan tautan
        status_content.append(
            f"| [{function_count}. {name.replace('_', ' ').title()}](#{function_count}-{formatted_name}) | "
        )

        # Format docstring untuk keterbacaan yang lebih baik
        formatted_docstring = format_docstring(docstring)

        # Penanganan khusus untuk fungsi `upload_image`
        if name == "upload_image":
            status = "✅"
            params_str = ", ".join(
                f"{param}='file/to/upload'" for param in signature.parameters
            )
            result = "Anda akan mendapatkan URL"
            # Dokumentasikan fungsi `upload_image` di README
            readme_content.append(
                f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                f"{formatted_docstring}\n\n"
                f"```python\nfrom ApiNyaEr import apinya\n\n"
                f"result = await apinya.{name}({params_str})\n"
                f"print(result)\n```\n\n"
                f"#### Hasil yang Diharapkan\n\n"
                f"```text\n{result}\n```\n"
            )
        else:
            # Tangani fungsi lain
            if len(signature.parameters) == 0:
                # Tidak ada parameter
                status, result = await test_method(method)
                # Tambahkan dokumentasi fungsi untuk fungsi tanpa parameter
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom ApiNyaEr import apinya\n\n"
                    f"result = await apinya.{name}()\n"
                    f"print(result)\n```\n\n"
                    f"#### Hasil yang Diharapkan\n\n"
                    f"{format_result(result)}\n"
                )
            else:
                # Tangani fungsi dengan parameter
                params = []
                for param in signature.parameters.values():
                    if param.default is not param.empty:
                        param_value = repr(param.default)
                        params.append(f"{param.name}={param_value}")
                    elif param.annotation is int:
                        params.append(f"{param.name}=5")
                    else:
                        params.append(f"{param.name}='Pokemon'")

                # Uji fungsi dengan parameter contoh
                status, result = await test_method(
                    method, *[eval(param.split("=")[1]) for param in params]
                )

                params_str = ", ".join(params)

                # Dokumentasikan fungsi dengan parameter di README
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom ApiNyaEr import apinya\n\n"
                    f"result = await apinya.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"#### Hasil yang Diharapkan\n\n"
                    f"{format_result(result)}\n"
                )

        # Perbarui status tabel dengan status fungsi
        status_content[-1] += status
        function_statuses.append((name, status))
        function_count += 1

    return status_content, readme_content


# Menulis status AI dan dokumentasi ke README.md
async def write_ai_status_to_file(
    status_content,
    readme_content,
    readme_file="README.md",
    separator="---",
    license_text="\nProyek ini dilisensikan di bawah [MIT License](https://github.com/ErRickow/ApiNyaEr/blob/main/LICENSE)",
):
    try:
        with open(readme_file, "r") as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = ""

    # Jika pemisah ada, hanya simpan bagian sebelum pemisah
    if separator in existing_content:
        pre_separator_content, _ = existing_content.split(separator, 1)
    else:
        pre_separator_content = existing_content

    # Bangun konten README yang baru
    status_str = "\n".join(status_content)
    new_content = "\n".join(readme_content)

    preface = "# 📘 Dokumentasi AI\n\n"
    preface += (
        "Selamat datang di **ErAI**! Perpustakaan ini memungkinkan Anda untuk berinteraksi dengan AI menggunakan opsi **sinkron** dan **asinkron**.\n\n"
        "- **Sync**: `from ApiNyaEr.sync import apinya`\n"
        "- **Async**: `from ApiNyaEr import apinya`\n\n"
        "Berikut, kami akan membahas setiap fungsi, memberikan contoh dan hasil yang diharapkan agar Anda bisa mulai dengan cepat! Mari kita mulai 🚀\n\n"
        "## Status\n\n"
        "| Fungsi             | Status |\n"
        "|--------------------|--------|\n"
        f"{status_str}\n\n"
    )

    updated_content = (
        pre_separator_content.strip() + "\n\n" + separator + "\n\n" + preface
    )
    updated_content += "\n## 🎓 Cara Menggunakan Setiap Fungsi\n\n" + new_content
    updated_content += "\n" + license_text

    async with aiofiles.open(readme_file, "w") as f:
        await f.write(updated_content)


# Fungsi utama untuk menjalankan skrip
async def main():
    methods = inspect.getmembers(
        apinya, predicate=lambda m: inspect.ismethod(m) or inspect.isfunction(m)
    )
    status_content, readme_content = await generate_ai_status(methods)
    await write_ai_status_to_file(status_content, readme_content)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import inspect
import aiofiles
from ApiNyaEr import ErApi, Musiknya

# Helper function to test each API method
async def test_method(method, *args):
    try:
        if inspect.iscoroutinefunction(method):
            result = await method(*args)  # If async, await the result
        else:
            result = method(*args)  # If sync, call directly
        status = "✅"  # Mark as successful
        return status, result
    except Exception as e:
        status = "❌"  # Mark as failed
        return status, str(e)

# Function to test the selected methods
async def test_selected_methods():
    erapi = ErApi()
    musiknya = Musiknya()

    # Test methods from ErApi
    erapi_methods = [
        (erapi.neko, "neko", 3),
        (erapi.password, 12)
    ]

    # Test methods from Musiknya
    musiknya_methods = [
        (musiknya.search, "Gue Mah Apah"),
        (musiknya.get_song_by_id, "some_song_id")
    ]

    results = []

    # Test ErApi methods
    for method, *args in erapi_methods:
        status, result = await test_method(method, *args)
        results.append(
            f"```python\nErApi.{method.__name__}({', '.join(map(str, args))})\nStatus: {status}, Result: {result}\n```"
        )

    # Test Musiknya methods
    for method, *args in musiknya_methods:
        status, result = await test_method(method, *args)
        results.append(
            f"```python\nMusiknya.{method.__name__}({', '.join(map(str, args))})\nStatus: {status}, Result: {result}\n```"
        )

    return results

# Function to update README with test results
async def update_readme(test_results):
    readme_file = "README.md"
    separator = "---"
    license_text = "\nThis Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)"

    try:
        async with aiofiles.open(readme_file, "r") as f:
            existing_content = await f.read()
    except FileNotFoundError:
        existing_content = ""

    # If separator exists, keep only the part before it
    if separator in existing_content:
        pre_separator_content, _ = existing_content.split(separator, 1)
    else:
        pre_separator_content = existing_content

    # Build the new README content
    test_results_str = "\n".join(test_results)
    new_content = (
        "### Test Results\n\n"
        "| Function | Status | Result |\n"
        "|----------|--------|--------|\n" + test_results_str + "\n"
    )

    updated_content = (
        pre_separator_content.strip()
        + "\n\n"
        + separator
        + "\n\n"
        + new_content
        + "\n"
        + license_text
    )

    async with aiofiles.open(readme_file, "w") as f:
        await f.write(updated_content)

# Main function to run the script
async def main():
    test_results = await test_selected_methods()
    await update_readme(test_results)

if __name__ == "__main__":
    asyncio.run(main())
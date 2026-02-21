from playwright.sync_api import sync_playwright
import re

seeds = range(84, 94)
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_selector("table")

        cells = page.query_selector_all("td")

        for cell in cells:
            value = cell.inner_text().strip()
            numbers = re.findall(r"-?\d+", value)
            for num in numbers:
                total_sum += int(num)

    browser.close()

print("FINAL TOTAL:", total_sum)

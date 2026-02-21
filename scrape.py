from playwright.sync_api import sync_playwright

seeds = range(36, 46)
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
            if value.isdigit():
                total_sum += int(value)

    browser.close()

print("FINAL TOTAL:", total_sum)

print("FINAL TOTAL:", total_sum)

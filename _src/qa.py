import sys, asyncio
from playwright.async_api import async_playwright
root, out = sys.argv[1], sys.argv[2]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w in [320, 375, 414, 768, 1024, 1440]:
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(f'file://{root}/index.html')
            await pg.wait_for_timeout(600)
            sw = await pg.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
            print(w, 'hscroll', sw, 'errors', errs)
            if w in (390, 375, 1440):
                await pg.screenshot(path=f'{out}/full_{w}.png', full_page=True)
            await pg.close()
        await b.close()
asyncio.run(main())

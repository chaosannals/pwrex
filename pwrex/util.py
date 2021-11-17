from playwright.async_api import Page

async def wait_ms(page: Page, t: int):
    '''
    分段等待，防止长等待导致命令长时间不被处理。
    '''

    while t > 0:
        i = min(t, 1000)
        t -= i
        await page.wait_for_timeout(i)

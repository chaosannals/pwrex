from playwright.async_api import Page, ElementHandle
from pwrex.util import wait_ms

async def pick_all(page: Page, selector, try_count=10) -> list[ElementHandle]:
    '''
    页面选中多个元素
    '''

    for i in range(try_count):
        r = await page.query_selector_all(selector=selector)
        if len(r) > 0:
            return r
        await page.wait_for_timeout(1000)
    return []


async def pick_one(page: Page, selector, try_count=10) -> ElementHandle:
    '''
    页面选中一个元素
    '''

    for i in range(try_count):
        r = await page.query_selector(selector=selector)
        if r is not None:
            return r
        await page.wait_for_timeout(1000)
    return None


async def e_pick_all(page: Page, e: ElementHandle, selector, try_count=10) -> list[ElementHandle]:
    '''
    元素选中多个子元素
    '''

    for i in range(try_count):
        r = await e.query_selector_all(selector=selector)
        if len(r) > 0:
            return r
        await wait_ms(page, 1000)
    return []


async def e_pick_one(page: Page, e: ElementHandle, selector, try_count=10) -> ElementHandle:
    '''
    元素选中一个子元素
    '''

    for i in range(try_count):
        r = await e.query_selector(selector=selector)
        if r is not None:
            return r
        await wait_ms(page, 1000)
    return None

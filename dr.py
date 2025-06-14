import asyncio
from pyppeteer import launch

# List of common ad/tracker domains or URL patterns to block
BLOCKED_RESOURCE_TYPES = ['image', 'media', 'font', 'texttrack', 'stylesheet', 'script', 'xhr', 'fetch', 'eventsource', 'websocket', 'manifest', 'other']
BLOCKED_URL_PARTS = [
    'ads', 'doubleclick.net', 'googlesyndication', 'adservice.google.com', 'googleadservices.com',
    'pagead2.googlesyndication.com', 'adserver', 'adbrite', 'adroll', 'advertising', 'analytics'
]

async def intercept_request(request):
    url = request.url.lower()
    if any(part in url for part in BLOCKED_URL_PARTS):
        await request.abort()
    else:
        await request.continue_()

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.setRequestInterception(True)
    page.on('request', intercept_request)

    await page.goto('https://dramabox.com')  # Replace with actual Dramabox URL

    # Your automation code here: play video, skip ads, etc.

    await asyncio.sleep(60)  # Keep browser open for 60 seconds to observe

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

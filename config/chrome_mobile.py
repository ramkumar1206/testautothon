from selenium import webdriver

def chrome_mobile():
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": (
            "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR6.170623.017) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile "
            "Safari/537.36"
        ),
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    return driver

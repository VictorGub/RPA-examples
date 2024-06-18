import rpa as r

URL = "https://agileengine.com/get-in-touch/"
NAME = "John"
LAST_NAME = "Doe"
EMAIL = "test@example.com"
COMPANY = "Test"
DD_OPTION = "Development solutions"

if __name__ == "__main__":
    if r.init(headless_mode=True):
        r.url(URL)
        r.type("//*[@name='Name_First']", NAME)
        r.type("//*[@name='Name_Last']", LAST_NAME)
        r.type("//*[@name='Email']", EMAIL)
        r.type("//*[@name='SingleLine']", COMPANY)
        r.select("//*[@name='Dropdown']", DD_OPTION)
        r.click("#DecisionBox")  # uncheck checkbox
        r.wait()
        r.snap("page", "result.png")
        r.close()

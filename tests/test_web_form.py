class TestWebForm:

    def test_submit_form(self, web_form):
        web_form.fill_text("Yaniv")
        web_form.submit()
        assert web_form.get_message() == "Received!"

    def test_page_title(self, driver):
        assert driver.title == "Web form"
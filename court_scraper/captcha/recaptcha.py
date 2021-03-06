from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Recaptcha:

    def _recaptcha_V2_solver(self):
        self.solver = recaptchaV2Proxyless()
        self.solver.set_verbose(0)
        self.solver.set_key(self.apikey)
        self.solver.set_website_url(self.driver.current_url)
        self.solver.set_website_key(self.sitekey)
        self.g_response = self.solver.solve_and_return_solution()
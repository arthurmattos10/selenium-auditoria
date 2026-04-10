from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dropdown")

print("Abas abertas:", len(driver.window_handles))

driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2');")

while len(driver.window_handles) < 2:
    time.sleep(0.5)

print("Segunda aba aberta!")

driver.switch_to.window(driver.window_handles[1])

print("URL aba 1:", driver.current_url)

driver.execute_script("window.open('https://pt.wikipedia.org');")

while len(driver.window_handles) < 3:
    time.sleep(0.5)

print("Terceira aba aberta!")

driver.switch_to.window(driver.window_handles[2])

print("URL aba 2:", driver.current_url)

print("Total de abas:", len(driver.window_handles))

# ===== PARTE 3: INTERAÇÃO COM DROPDOWN =====

driver.switch_to.window(driver.window_handles[0])
print("Voltando para aba 0:", driver.current_url)


dropdown_element = driver.find_element(By.ID, "dropdown")

select = Select(dropdown_element)

select.select_by_visible_text("Option 1")

print("Option 1 selecionada")


selected_option = select.first_selected_option

value = selected_option.get_attribute("value")

print("Valor selecionado:", value)

driver.quit()
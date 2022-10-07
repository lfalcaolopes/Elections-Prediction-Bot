from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from website_confirmations import WebsiteConfirmation
from data_formating import DataFormatting

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

confirmations = WebsiteConfirmation(driver)
formatting = DataFormatting()

statesx = {"ac": 455903, "al": 1805971, "ap": 442842, "am": 2113551, "ba": 8874841, "df": 1819900, "es": 2315889,
          "zz": 304032, "go": 3812597, "ma": 3920435, "mt": 1892180, "ms": 1555149, "mg": 12655228, "pr": 6828543,
          "pb": 2557479, "pa": 4789311, "pe": 5738371, "pi": 2115645, "rj": 9909463, "rn": 2090604, "rs": 6890016,
          "ro": 926827, "rr": 305404, "sc": 4487474, "se": 1364724, "sp": 27189714, "to": 891449}

states = {"ac": 455903, "al": 1805971}



driver.get("https://resultados.tse.jus.br/oficial/app/index.html#/m/eleicao/resultados")
driver.maximize_window()

sleep(1)
lula_total_votes = 0
bolsonaro_total_votes = 0
total_votes = 0

# confirmations.websiteConfirmations()  # Don't have to use when the window go full screen

for state, state_votes in states.items():
    print(state)
    url = f"https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e544;uf={state};ufbu={state}/resultados"

    driver.get(url)
    sleep(1)

    candidates = driver.find_elements(By.CSS_SELECTOR, "div.text-gray-550")[0:2]
    votes = driver.find_elements(By.CSS_SELECTOR, "div.text-gray-600")[0:2]
    percentage = driver.find_elements(By.CSS_SELECTOR, "div.text-ion-tertiary")[0:2]

    if candidates[0].text == "PT – 13":
        lula_votes, bolsonaro_votes = list(map(formatting.votes, votes))
        lula_percentage, bolsonaro_percentage = list(map(formatting.percentage, percentage))
    elif candidates[0].text == "PL – 22":
        bolsonaro_votes, lula_votes = list(map(formatting.votes, votes))
        bolsonaro_percentage, lula_percentage = list(map(formatting.percentage, percentage))
    else:
        print("something went wrong")

    # print("lula", lula_percentage, "bolso", bolsonaro_percentage)

    lula_total_votes += int(state_votes * lula_percentage)
    bolsonaro_total_votes += int(state_votes * bolsonaro_percentage)
    total_votes += state_votes

lula_total_percentage = str((lula_total_votes / total_votes) * 100) + "%"
bolsonaro_total_percentage = str(bolsonaro_total_votes / total_votes * 100) + "%"

print("lula", lula_total_votes, "bolsonaro", bolsonaro_total_votes)
print("lula", lula_total_percentage, "bolsonaro", bolsonaro_total_percentage)

# sections_percentage = driver.find_element(By.CSS_SELECTOR, "div[class = 'flex flex-row items-center']")

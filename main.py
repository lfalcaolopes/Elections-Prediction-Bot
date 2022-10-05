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

states = {"ac": 455903, "al": 1805971, "ap": 442842, "am": 2113551, "ba": 8874841, "df": 1819900, "es": 2315889,
          "zz": 304032, "go": 3812597, "ma": 3920435, "mt": 1892180, "ms": 1555149, "mg": 12655228, "pr": 6828543,
          "pb": 2557479, "pa": 4789311, "pe": 5738371, "pi": 2115645, "rj": 9909463, "rn": 2090604, "rs": 6890016,
          "ro": 926827, "rr": 305404, "sc": 4487474, "se": 1364724, "sp": 27189714, "to": 891449}

state = "ba"

url = f"https://resultados.tse.jus.br/oficial/app/index.html#/eleicao;e=e544;uf={state};ufbu={state}/resultados"

driver.get("https://resultados.tse.jus.br/oficial/app/index.html#/m/eleicao/resultados")

sleep(0.5)

confirmations.websiteConfirmations()

driver.get(url)
sleep(1)

candidates = driver.find_elements(By.CSS_SELECTOR, "div.text-gray-700")[0:2]
votes = driver.find_elements(By.CSS_SELECTOR, "div.text-gray-600")[0:2]
percentage = driver.find_elements(By.CSS_SELECTOR, "div.text-ion-tertiary")[0:2]

# if candidates[0].text == "LULA":
lulaVotes, bolsonaroVotes = list(map(formatting.votes, votes))
lulaPercentage, bolsonaroPercentage = list(map(formatting.percentage, percentage))

print(lulaVotes, bolsonaroVotes)
print(lulaPercentage, bolsonaroPercentage)


# sections_percentage = driver.find_element(By.CSS_SELECTOR, "div[class = 'flex flex-row items-center']")

# print(candidates[0].text.split(" ")[0].replace(".", ""))
# print(candidates[1].text.split(" ")[1].replace(".", ""))

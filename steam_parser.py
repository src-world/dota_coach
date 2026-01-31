import requests
from bs4 import BeautifulSoup
import logging
import currency_converter as cc



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_top_deals(limit=10):
    """
    Парсит страницу Steam и возвращает список словарей с информацией о топ-X играх со скидкой.
    """
    url = "http://store.steampowered.com/search/?specials=1&os=win"
    deals = []
    
    try:
        r = requests.get(url, timeout=10) # Добавляем таймаут
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при запросе к Steam: {e}")
        return []

    soup = BeautifulSoup(r.content, "html.parser")
    game_rows = soup.find_all('a', class_='search_result_row')

    for row in game_rows:
        name_tag = row.find('span', class_='title').text
        discount_tag = row.find('div', class_='discount_pct').text
        original_price = row.find('div', class_='discount_original_price').text
        discount_price = row.find('div', class_='discount_final_price').text
        game_url = row['href']

        deals.append({
            "name": name_tag,
            "skidka": discount_tag,
            "start_price": original_price,
            "exit_prive": discount_price,
            "game_ul": game_url
        })
        
        if len(deals) >= limit: # Ограничиваем количество игр
            break
            
            
    return deals

    message = f"🎮 - Название : {dict.get("name")}\n\n🎁 - Скидка : {dict.get("skidka")}\n\n💸 - Обычная цена : {dict.get("start_price")}\n\n💸 - Текущая цена : {dict.get("exit_prive")}"

if __name__ == '__main__':
    # Пример использования
    deals = get_top_deals(limit=5)
    if deals:
        for deal in deals:
            print(deal)
    else:
        print("Не удалось получить информацию о сделках.")
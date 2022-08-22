from playwright.sync_api import sync_playwright
import time


def bot():

    list_note_lenovo = []
    try:
        with sync_playwright() as  p:
            nav = p.chromium.launch(headless=False)
            page = nav.new_page()
            page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
            all_product = page.query_selector_all('.caption')
            for product in all_product:
                titulo = product.query_selector('.title').inner_text()
                if titulo.startswith("Lenovo"):
                    descricao = product.query_selector('.description').inner_text()
                    preco = product.query_selector('.price').inner_text() 
                    price = preco.replace('$', '')
                    price = float(price)
                    list_note_lenovo.append({'titulo': titulo, 'descricao': descricao, 'preco': preco})
            
            print(list_note_lenovo)
            time.sleep(5)
            nav.close()
        return list_note_lenovo
    except:
        print('Erro interno :(')



if __name__ == '__main__':
    bot()

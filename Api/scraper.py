from playwright.sync_api import sync_playwright, TimeoutError


def bot():
    
 
    with sync_playwright() as  p:
        nav = p.chromium.launch()
        page = nav.new_page()
        page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
        lenovo = []
        try:
            all_product = page.query_selector_all('.caption')
            for product in all_product:
                titulo = product.query_selector('.title').inner_text()
                if titulo.startswith("Lenovo"):
                    titulo = product.query_selector('.title').inner_text()
                    descricao = product.query_selector('.description').inner_text()
                    preco = product.query_selector('.price').inner_text()
                    lenovo.append({'titulo': titulo,'descrição': descricao,'Preço': preco})
            print(lenovo)
        except TimeoutError as err:
            print(f"Erro :( tente mais uma vez {err}")
                    
        nav.close()
        return lenovo



if __name__ == '__main__':
    bot()
        
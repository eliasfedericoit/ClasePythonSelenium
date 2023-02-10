from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://automationexercise.com/products')
driver.find_element('name', 'search').send_keys('hola')
driver.find_element('id', 'submit_search').click()
input("Presiona enter para cerrar la ventana del navegador") #este input hace que no se cierre la ventana automáticamente al final
#driver.close()
#driver.quit()
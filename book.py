import pdfkit
for i in range(273,352):
    print('Печатаю', i, 'страницу')
    x = '{:04}'.format(i)
    url = f'https://bmstu.press/ebooks/2021/03/05/c3530b7d86ec06779b9c43b2cad99de6/OEBPS/mybook{x}.xhtml'
    pdfkit.from_url(url, f'book{i}.pdf')
    print('Напечатал', i, 'страницу')

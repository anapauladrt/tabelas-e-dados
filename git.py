import openpyxl
tabela=openpyxl.load_workbook('tabela.xlsx')
dados_page= tabela['dados']
#imprimindo dados de cada linha
for rows in dados_page.iter_rows(min_row=1, max_row=20):
    for cell in rows:
        print(cell.value)
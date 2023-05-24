import openpyxl as excel

# Cabeçalho da planilha
headers = [
    "nperfil",
    "c1",
    "c2",
    "c3",
    "c4",
    "beta1",
    "beta2",
    "beta3",
    "beta4",
    "B",
    "R",
    "Vax",
    "omega",
    "R_hub",
    "R_root",
    "eff",
    "T",
    "Q",
]


def write_to_excel(helices_matrix: list[list]):
    wb = excel.Workbook()
    ws = wb.active

    # Escrever o cabeçalho primeiro
    for idx, header in enumerate(headers):
        ws.cell(row=1,column=(idx+1)).value = header

    # Escrever os valores da matrix de dados das helices
    for row in helices_matrix:
        ws.append(row)
    
    wb.save("results.xlsx")

#helices_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#write_to_excel(helices_matrix)

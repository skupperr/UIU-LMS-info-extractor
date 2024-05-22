import xlsxwriter


def creating_excel_file(file_name, queue, queue2):
    workbook = xlsxwriter.Workbook(f"{file_name}.xlsx")
    worksheet = workbook.add_worksheet("firstsheet")

    worksheet.write(0, 0, "#")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "ID")
    worksheet.write(0, 3, "Email")

    worksheet.set_column(1,1,30)
    worksheet.set_column(2,2,15)
    worksheet.set_column(3,3,70)

    i = 1
    while(not queue.empty()):
        a = queue.get()
        worksheet.write(i, 0, str(i))
        worksheet.write(i, 1, a["name"])
        worksheet.write(i, 2, a["id"])
        worksheet.write(i, 3, a["email"])
        i+=1

    while(not queue2.empty()):
        a = queue2.get()
        worksheet.write(i, 0, str(i))
        worksheet.write(i, 1, a["name"])
        worksheet.write(i, 2, a["id"])
        worksheet.write(i, 3, a["email"])
        i+=1

    workbook.close()
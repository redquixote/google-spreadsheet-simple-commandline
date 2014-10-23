import gspread
import click


@click.command()
@click.option('--user', help='valid google username.')
@click.option('--password', help='password to access the document')
@click.option('--spreadsheet', help='spreadsheet name')
@click.option('--sheet_number', default=0, help='which sheet to update')
@click.option('--col', default=1, help='column number to add the value')
@click.option('--row', help='row number. Default last empty row.')
@click.option('--value', help='optional. value to add. if not stdin specify')
def spreadsheet_append(user, password, spreadsheet, value,
                       sheet_number=0,
                       col=1,
                       row=0):
    # Login with your Google account
    gc = gspread.login(user, password)

    sps = gc.open(spreadsheet)
    wks = sps.get_worksheet(sheet_number)

    if not row:
        all_wks = wks.get_all_records()
        row = len(all_wks) + 2
    wks.update_cell(row, col, value)


if __name__ == '__main__':
    spreadsheet_append()

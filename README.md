Google Spreadsheet Simple Command Line
====================================

Simple command line to update Google Spreadsheets.

        Usage: gs.py [OPTIONS]

        Options:
          --user TEXT             valid google username.
          --password TEXT         password to access the document
          --spreadsheet TEXT      spreadsheet name
          --sheet_number INTEGER  which sheet to update
          --col INTEGER           column number to add the value
          --row TEXT              row number. Default last empty row.
          --value TEXT            optional. value to add. if not stdin specify
          --help                  Show this message and exit.


Example:

    python gs.py --user=xyz@gmail.com --password=mypassword --spreadsheet="Calculations" --col=3 --value="new value way"
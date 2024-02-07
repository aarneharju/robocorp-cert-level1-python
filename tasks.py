from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    browser.configure(
        #slowmo=1000,
    )
    open_the_intranet_website()
    log_in()
    download_the_excel_file()
    fill_form_with_excel_data()

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""

    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")

def fill_and_submit_the_sales_form(sales_rep):
    """Fills in the sales data and clicks the submit button"""
    page = browser.page()
    page.fill("#firstname", sales_rep["First Name"])
    page.fill("#lastname", sales_rep["Last Name"])
    page.select_option("#salestarget", str(sales_rep["Sales Target"]))
    page.fill("#salesresult", str(sales_rep["Sales"]))
    page.click("text=Submit")

def download_the_excel_file():
    """Downloads the Excel file from the given URL"""
    http = HTTP()
    http.download("https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)
    
def fill_form_with_excel_data():
    """Read data from Excel and fill in the sales form"""
    excel = Files()
    excel.open_workbook("SalesData.xlsx")
    worksheet = excel.read_worksheet_as_table("data", header=True)
    excel.close_workbook()

    for row in worksheet:
        fill_and_submit_the_sales_form(row)
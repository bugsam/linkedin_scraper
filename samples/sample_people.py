from linkedin_scraper import Person, actions
from selenium import webdriver
import xlsxwriter

def createWorksheet(person, worksheet, row, col):
    
    worksheet.write_url(row, col, person.linkedin_url)
    worksheet.write_string(row, col + 1, person.name)
    worksheet.write_row(row, col + 1, person.also_viewed_urls)
    worksheet.write_row(row, col + 1, person.about)
    worksheet.write_row(row, col + 1, person.accomplishments)
    worksheet.write_string(row, col + 1, person.company)
    worksheet.write_string(row, col + 1, person.job_title)
    worksheet.write_string(row, col + 1, person.location)
    worksheet.write_boolean(row, col + 1, person.open_to_work)
    
    for ed in person.educations:
        worksheet.write(row, col + 1, ed.company_size)
        worksheet.write_string(row, col + 1, ed.degree)
        if type(ed.description) is str: 
            worksheet.write_string(row, col + 1, ed.description)
        else:
            worksheet.write_row(row, col + 1, "empty") 
        worksheet.write(row, col + 1, ed.founded)
        worksheet.write(row, col + 1, ed.from_date)
        worksheet.write(row, col + 1, ed.headquarters)
        worksheet.write(row, col + 1, ed.industry)
        worksheet.write_string(row, col + 1, ed.institution_name)
        worksheet.write_url(row, col + 1, ed.linkedin_url)
        worksheet.write(row, col + 1, ed.to_date)
        worksheet.write(row, col + 1, ed.type)
        worksheet.write(row, col + 1, ed.website)
        
    for ex in person.experiences:
        worksheet.write(row, col + 1, ex.company_size)
        if type(ex.description) is str:
            worksheet.write_row(row, col + 1, ex.description)
        else:
             worksheet.write_row(row, col + 1, "empty")
        worksheet.write(row, col + 1, ex.duration)
        worksheet.write(row, col + 1, ex.founded)
        worksheet.write_row(row, col + 1, ex.from_date)
        worksheet.write(row, col + 1, ex.headquarters)
        worksheet.write(row, col + 1, ex.industry)
        worksheet.write_row(row, col + 1, ex.institution_name)
        worksheet.write_row(row, col + 1, ex.linkedin_url)
        worksheet.write_row(row, col + 1, ex.location)
        worksheet.write_row(row, col + 1, ex.position_title)
        worksheet.write_row(row, col + 1, ex.to_date)
        worksheet.write(row, col + 1, ex.type)
        worksheet.write(row, col + 1, ex.website)
        
    return row

# driver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# credentials
email = "";
password = "";

# getting all linkedin profiles
people = ["jonmacaskill", "andrew-huberman"]

# creating the Excel
workbook = xlsxwriter.Workbook('people.xlsx')
worksheet = workbook.add_worksheet()
row = 0;
col = 0;

for p in people:
    driver = webdriver.Chrome(options=options)
    actions.login(driver, email, password)
    url = "https://www.linkedin.com/in/" + p
    person = Person(linkedin_url=url, driver=driver)
    createWorksheet(person, worksheet, row, col)
    row += 1

workbook.close()

from linkedin_scraper import Person, actions
from selenium import webdriver
import xlsxwriter

def createWorksheet(person, workbook, row, row_ed, row_ex):

    col = 0;
    principal.write_url(row, col, person.linkedin_url)
    principal.write_string(row, col, person.name)
    col += 1
    if person.also_viewed_urls:
        for av in person.also_viewed_urls:
            principal.write(row, col, av)
            col += 1
    else:
        principal.write(row, col, "also_viewed_urls:empty")
        col += 1

    principal.write(row, col, person.about)
    col += 1

    if person.accomplishments:
        for acc in person.accomplishments:
            principal.write(row, col, person.accomplishments)
            col += 1
    else:
        principal.write(row, col, "accomplishments:empty")
        col += 1

    principal.write_string(row, col, person.company)
    col += 1

    principal.write_string(row, col, person.job_title)
    col += 1

    principal.write_string(row, col, person.location)
    col += 1

    principal.write_boolean(row, col, person.open_to_work)
    col += 1

    for ed in person.educations:
        col_ed = 0
        educations.write(row_ed, col_ed, person.linkedin_url)
        col_ed += 1
        educations.write(row_ed, col_ed, ed.company_size)
        col_ed += 1
        educations.write_string(row_ed, col_ed, ed.degree)
        col_ed += 1
        
        if type(ed.description) is str: 
            educations.write_string(row_ed, col_ed, ed.description)
        else:
            educations.write_row(row_ed, col_ed, "education_description:empty")
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.founded)
        col_ed += 1    
        
        educations.write(row_ed, col_ed, ed.from_date)
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.headquarters)
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.industry)
        col_ed += 1
        
        educations.write_string(row_ed, col_ed, ed.institution_name)
        col_ed += 1
        
        educations.write_url(row_ed, col_ed, ed.linkedin_url)
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.to_date)
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.type)
        col_ed += 1
        
        educations.write(row_ed, col_ed, ed.website)
        row_ed += 1

    for ex in person.experiences:
        col_ex = 0 
        experiences.write(row_ex, col_ex, person.linkedin_url)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.company_size)
        col_ex += 1
        if type(ex.description) is str:
            experiences.write(row_ex, col_ex, ex.description)
        else:
             experiences.write(row_ex, col_ex, "empty")
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.duration)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.founded)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.from_date)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.headquarters)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.industry)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.institution_name)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.linkedin_url)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.location)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.position_title)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.to_date)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.type)
        col_ex += 1
        experiences.write(row_ex, col_ex, ex.website)
        row_ex += 1
    
    return row, row_ed, row_ex

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
workbook = xlsxwriter.Workbook('2023-01.xlsx')
principal = workbook.add_worksheet("principal")
educations = workbook.add_worksheet("educations")
experiences = workbook.add_worksheet("experiences")
row = 0;
row_ed = 0
row_ex = 0

for p in people:
    driver = webdriver.Chrome(options=options)
    value = random.randint(1, 20)
    driver.implicitly_wait(value)
    try:
        element = WebDriverWait(driver, 90).until(
            actions.login(driver, email, password)
        )
    finally:
        driver.quit()

    url = "https://www.linkedin.com/in/" + p
    person = Person(linkedin_url=url, driver=driver)
    value = random.randint(1, 10)
    driver.implicitly_wait(value)
    (row, row_ed, row_ex) = createWorksheet(person, workbook, row, row_ed, row_ex)
    row += 1

workbook.close()

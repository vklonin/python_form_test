from selenium.webdriver.support.ui import Select
from selene.support.shared import browser
from selene import be, have

def test_of_student_form():

    # page object
    browser.open('https://demoqa.com/automation-practice-form')
    first_name = browser.element("#firstName")
    last_name = browser.element("#lastName")
    user_email = browser.element("#userEmail")
    user_number = browser.element("#userNumber")
    gender_selector = browser.elements(".custom-radio")
    date_of_birth = browser.element(".react-datepicker-wrapper")
    subjects = browser.element('#subjectsInput')
    hobbies_selector = browser.elements('.custom-checkbox')
    upload_button = browser.element('input[id=uploadPicture]')
    current_address = browser.element('#currentAddress')
    state_selector = browser.element('#state')
    city_selector = browser.element('#city')
    submit_button = browser.element('#submit')

    first_name.set_value("Ranga")
    last_name.set_value("Caranam")
    user_email.set_value("Ranga@Caranam.com")
    gender_selector.filtered_by_their('label', have.text('Other')).element(0).click()
    user_number.set_value("9156200011")

    # filling a date 06 of March 1978
    date_of_birth.click()
    select_month = Select(browser.element('.react-datepicker__month-select').get_actual_webelement())
    select_month.select_by_index(2)  # real month - 1
    select_year = Select(browser.element('.react-datepicker__year-select').get_actual_webelement())
    select_year.select_by_value('1978')  # actual year
    browser.element(".react-datepicker__day--006").click()  # actual day of month

    # browser.element('.react-datepicker__month-select').click()
    subjects.send_keys("Math").press_enter()
    subjects.send_keys("Chem").press_enter()

    hobbies_selector.filtered_by_their('label', have.text('Sports')).element(0).click()
    hobbies_selector.filtered_by_their('label', have.text('Music')).element(0).click()

    upload_button.send_keys("/Users/vladimirklonin/Documents/file.png")

    current_address.send_keys("445045, a string with address").press_tab()
    state_selector.click().element('input').send_keys("NCR").press_tab()
    city_selector.click().element('input').send_keys('Delhi').press_tab().press_enter()

    # validation data
    validation_pairs = [ ("Student Name",	"Ranga Caranam"),
                         ("Student Email",	"Ranga@Caranam.com"),
                         ("Gender", "Other"),
                         ("Mobile", "9156200011"),
                         ("Date of Birth", "06 March,1978"),
                         ("Subjects", "Maths, Chemistry"),
                         ("Hobbies", "Sports, Music"),
                         ("Picture", "file.png"),
                         ("Address", "445045, a string with address"),
                         ("State and City", "NCR Delhi")]

    # validation
    browser.element('.modal-header').should(have.text("Thanks for submitting the form"))
    table_rows = browser.element('tbody').elements('tr')

    for row, validation_row in zip(table_rows, validation_pairs):
        assert row.elements('td').element(0).text == validation_row[0]
        assert row.elements('td').element(1).text == validation_row[1]

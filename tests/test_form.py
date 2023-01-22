import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from demoqa_test.model.pages.practise_form import PractiseFormPage
from demoqa_test.model.data.user import User
from demoqa_test.utils import attach

# browser.config.hold_browser_open = True
practise_form = PractiseFormPage()


@allure.title('Successful completion of the registration form')
@allure.tag('web', 'user', 'registration')
@allure.link('https://demoqa.com/automation-practice-form', name='Registration form')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'K1LLsound')
def test_form_registration():
    user = User(first_name='Sergey',
                last_name='QA',
                email='example@pochta.com',
                gender='Male',
                number='8800553555',
                date_year='1999',
                date_month='July',
                date_day=11,
                subjects='Maths',
                hobby='Music',
                picture='picture/stich.jpg',
                address='street Pushkina, home 5',
                state='NCR',
                city='Delhi')
    with allure.step('Open registration form'):
        practise_form.open_registration_form()

    with allure.step('Fill form'):
        practise_form.fill_registration_fields(user).submit()

    with allure.step('Check results'):
        practise_form.check_results(user)


    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
from selene import browser, be, have


def test_search_successful():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_empty():
    text_search = 'fhfjkk119191101j!!!&^*%$f'
    browser.element('[name="q"]').should(be.blank).type(text_search).press_enter()
    browser.element('[class="card-section"]').should(have.text(
        f'Your search - {text_search} - did not match any documents.'
    ))


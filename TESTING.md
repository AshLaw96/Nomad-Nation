# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory         | File                                                                                                                                        | URL                                                                                                                                                                                     | Screenshot                                                               | Notes                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------- |
| templates         | [base.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/base.html)                                                         | [HTML W3C Validator Link](https://validator.w3.org/nu/#textarea)                                                                                                                        | ![screenshot](documentation/validation/html/base.png)                    | Direct input, failed because of Django code   |
| templates         | [404.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/404.html)                                                           | [HTML W3C Validator Link](https://validator.w3.org/nu/#textarea)                                                                                                                        | ![screenshot](documentation/validation/html/404.png)                     | Source code input, no errors                  |
| templates         | [500.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/500.html)                                                           | [HTML W3C Validator Link](https://validator.w3.org/nu/#textarea)                                                                                                                        | ![screenshot](documentation/validation/html/500.png)                     | Source code input, no errors                  |
| templates/account | [login.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/login.html)                                               | [HTML W3C Validator Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/admin.py)                                                      | ![screenshot](documentation/validation/html/login.png)                   | All clear, no errors                          |
| templates/account | [logout.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/logout.html)                                             | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F)                                                 | ![screenshot](documentation/validation/html/logout.png)                  | All clear, no errors                          |
| templates/account | [password_reset_done.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/password_reset_done.html)                   | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Fpassword%2Freset%2Fkey%2F4-set-password%2F)               | ![screenshot](documentation/validation/html/password-reset-done.png)     | All clear, no errors                          |
| templates/account | [password_reset_from_key_done.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/password_reset_from_key_done.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Fpassword%2Freset%2Fkey%2Fdone%2F)                         | ![screenshot](documentation/validation/html/password-reset-key-done.png) | All clear, no errors                          |
| templates/account | [password_reset_from_key.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/password_reset_from_key.html)           | [HTML W3C Validator Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/views.py)                                                      | ![screenshot](documentation/validation/html/password-reset-key.png)      | Errors showing but from externally added code |
| templates/account | [password_reset.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/password_reset.html)                             | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F)                                      | ![screenshot](documentation/validation/html/password-reset.png)          | All clear, no errors                          |
| templates/account | [signup.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/templates/account/signup.html)                                             | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Fsignup%2F)                                                | ![screenshot](documentation/validation/html/signup.png)                  | Errors showing but from externally added code |
| dashboard         | [dashboard.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/templates/dashboard/dashboard.html)                           | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fdashboard%2F)                        | ![screenshot](documentation/validation/html/dash.png)                    | All clear, no errors                          |
| listings          | [add_caravan.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/templates/listings/add_caravan.html)                         | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Flistings%2Fadd%2F)                   | ![screenshot](documentation/validation/html/add-caravan.png)             | All clear, no errors                          |
| listings          | [booking.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/templates/listings/booking.html)                                 | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Flistings%2Fbookings%2F)              | ![screenshot](documentation/validation/html/book.png)                    | All clear, no errors                          |
| listings          | [listing_page.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/templates/listings/listing_page.html)                       | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Flistings%2Flistings%2F)              | ![screenshot](documentation/validation/html/list.png)                    | All clear, no errors                          |
| main              | [contact.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/templates/main/contact.html)                                         | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Fcontact%2F)                                                          | ![screenshot](documentation/validation/html/contact.png)                 | All clear, no errors                          |
| main              | [home.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/templates/main/home.html)                                               | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2F)                                                                    | ![screenshot](documentation/validation/html/home.png)                    | All clear, no errors                          |
| user_settings     | [account_settings.html](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/templates/user_settings/account_settings.html)     | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnomad-nation-23b17dd0a6b5.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fuser_settings%2Faccount_settings%2F) | ![screenshot](documentation/validation/html/account.png)                 | All clear no errors                           |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory  | File                                                                                   | URL                                                                                                                          | Screenshot                                          | Notes                                           |
| ---------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------- |
| static/css | [styles.css](https://github.com/AshLaw96/Nomad-Nation/blob/main/static/css/styles.css) | [HTML W3C Validator Link](https://jigsaw.w3.org/css-validator/validator?uri=https://nomad-nation-23b17dd0a6b5.herokuapp.com) | ![screenshot](documentation/validation/css/css.png) | Errors showing but from externally added styles |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File                                                                                | URL                           | Screenshot                                             | Notes                |
| --------- | ----------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------ | -------------------- |
| static/js | [script.js](https://github.com/AshLaw96/Nomad-Nation/blob/main/static/js/script.js) | [JSHint](https://jshint.com/) | ![screenshot](documentation/validation/js/js-hint.png) | All clear, no errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory       | File                                                                                                            | URL                                                                                                                                              | Screenshot                                                          | Notes                |
| --------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | -------------------- |
| caravan_booking | [settings.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/caravan_booking/py/settings.py)                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/caravan_booking/settings.py)            | ![screenshot](documentation/validation/py/settings.png)             | All clear, no errors |
| caravan_booking | [urls.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/caravan_booking/urls.py)                           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/caravan_booking/urls.py)                | ![screenshot](documentation/validation/py/caravan-book-urls.png)    | All clear, no errors |
| caravan_booking | [views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/caravan_booking/views.py)                         | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/caravan_booking/views.py)               | ![screenshot](documentation/validation/py/caravan-book-view.png)    | All clear, no errors |
| main            | [admin.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/admin.py)                                    | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/admin.py)                          | ![screenshot](documentation/validation/py/main-admin.png)           | All clear, no errors |
| main            | [models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/models.py)                                  | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/models.py)                         | ![screenshot](documentation/validation/py/main-models.png)          | All clear, no errors |
| main            | [test_forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/tests/test_forms.py)                    | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/tests/test_forms.py)               | ![screenshot](documentation/validation/py/main-form-test.png)       | All clear, no errors |
| main            | [test_models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/tests/test_models.py)                  | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/tests/test_models.py)              | ![screenshot](documentation/validation/py/main-models-test.png)     | All clear, no errors |
| main            | [test_views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/tests/test_views.py)                    | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/tests/test_views.py)               | ![screenshot](documentation/validation/py/main-view-test.png)       | All clear, no errors |
| main            | [urls.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/urls.py)                                      | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/urls.py)                           | ![screenshot](documentation/validation/py/main-urls.png)            | All clear, no errors |
| main            | [views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/views.py)                                    | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/views.py)                          | ![screenshot](documentation/validation/py/main-view.png)            | All clear, no errors |
| main            | [forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/main/forms.py)                                    | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/main/forms.py)                          | ![screenshot](documentation/validation/py/main-form.png)            | All clear, no errors |
| dashboard       | [admin.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/admin.py)                               | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/admin.py)                     | ![screenshot](documentation/validation/py/dash-admin.png)           | All clear, no errors |
| dashboard       | [models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/models.py)                             | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/models.py)                    | ![screenshot](documentation/validation/py/dash-model.png)           | All clear, no errors |
| dashboard       | [test_forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/tests/test_forms.py)               | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/tests/test_forms.py)          | ![screenshot](documentation/validation/py/dash-form-test.png)       | All clear, no errors |
| dashboard       | [test_models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/tests/test_models.py)             | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/tests/test_models.py)         | ![screenshot](documentation/validation/py/dash-model-test.png)      | All clear, no errors |
| dashboard       | [test_views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/tests/test_views.py)               | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/tests/test_views.py)          | ![screenshot](documentation/validation/py/dash-view-test.png)       | All clear, no errors |
| dashboard       | [urls.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/urls.py)                                 | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/urls.py)                      | ![screenshot](documentation/validation/py/dash-urls.png)            | All clear, no errors |
| dashboard       | [views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/views.py)                               | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/views.py)                     | ![screenshot](documentation/validation/py/dash-view.png)            | All clear, no errors |
| dashboard       | [forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/dashboard/forms.py)                               | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/dashboard/forms.py)                     | ![screenshot](documentation/validation/py/dash-form.png)            | All clear, no errors |
| listings        | [admin.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/admin.py)                                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/admin.py)                      | ![screenshot](documentation/validation/py/list-admin.png)           | All clear, no errors |
| listings        | [models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/models.py)                              | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/models.py)                     | ![screenshot](documentation/validation/py/list-models.png)          | All clear, no errors |
| listings        | [test_forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/tests/test_forms.py)                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/tests/test_forms.py)           | ![screenshot](documentation/validation/py/list-form-test.png)       | All clear, no errors |
| listings        | [test_models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/tests/test_models.py)              | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/tests/test_models.py)          | ![screenshot](documentation/validation/py/list-models-test.png)     | All clear, no errors |
| listings        | [test_views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/tests/test_views.py)                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/tests/test_views.py)           | ![screenshot](documentation/validation/py/list-views-test.png)      | All clear, no errors |
| listings        | [urls.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/urls.py)                                  | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/urls.py)                       | ![screenshot](documentation/validation/py/list-urls.png)            | All clear, no errors |
| listings        | [views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/views.py)                                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/views.py)                      | ![screenshot](documentation/validation/py/list-view.png)            | All clear, no errors |
| listings        | [forms.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/listings/forms.py)                                | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/listings/forms.py)                      | ![screenshot](documentation/validation/py/list-form.png)            | All clear, no errors |
| user_settings   | [admin.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/admin.py)                           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/admin.py)                 | ![screenshot](documentation/validation/py/user-admin.png)           | All clear, no errors |
| user_settings   | [models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/models.py)                         | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/models.py)                | ![screenshot](documentation/validation/py/user-models.png)          | All clear, no errors |
| user_settings   | [test_currency.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/tests/test_currency.py)     | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/tests/test_currency.py)   | ![screenshot](documentation/validation/py/user-currency-test.png)   | All clear, no errors |
| user_settings   | [test_models.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/tests/test_models.py)         | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/tests/test_models.py)     | ![screenshot](documentation/validation/py/user-model-test.png)      | All clear, no errors |
| user_settings   | [test_views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/tests/test_views.py)           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/tests/test_views.py)      | ![screenshot](documentation/validation/py/user-view-test.png)       | All clear, no errors |
| user_settings   | [test_middleware.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/tests/test_middleware.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/tests/test_middleware.py) | ![screenshot](documentation/validation/py/user-middleware-test.png) | All clear, no errors |
| user_settings   | [test_processors.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/tests/test_processors.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/tests/test_processors.py) | ![screenshot](documentation/validation/py/user-processor-test.png)  | All clear, no errors |
| user_settings   | [urls.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/urls.py)                             | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/urls.py)                  | ![screenshot](documentation/validation/py/user-urls.png)            | All clear, no errors |
| user_settings   | [views.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/views.py)                           | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/views.py)                 | ![screenshot](documentation/validation/py/user-view.png)            | All clear, no errors |
| user_settings   | [context_processors.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/context_processors.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/context_processors.py)    | ![screenshot](documentation/validation/py/user-processor.png)       | All clear, no errors |
| user_settings   | [currency.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/currency.py)                     | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/currency.py)              | ![screenshot](documentation/validation/py/user-currency.png)        | All clear, no errors |
| user_settings   | [middleware.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/user_settings/middleware.py)                 | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/user_settings/middleware.py)            | ![screenshot](documentation/validation/py/user-middleware.png)      | All clear, no errors |
|                 | [manage.py](https://github.com/AshLaw96/Nomad-Nation/blob/main/manage.py)                                       | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/AshLaw96/Nomad-Nation/main/manage.py)                              | ![screenshot](documentation/validation/py/manage.png)               | All clear, no errors |

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page                    | Mobile                                                                             | Tablet                                                                             | Desktop                                                                              | Notes             |
| ----------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------- |
| Register                | ![screenshot](documentation/responsiveness/mobile/mob-register.jpg)                | ![screenshot](documentation/responsiveness/tablet/tab-register.jpg)                | ![screenshot](documentation/responsiveness/desktop/desk-register.png)                | Works as expected |
| Login                   | ![screenshot](documentation/responsiveness/mobile/mob-login.jpg)                   | ![screenshot](documentation/responsiveness/tablet/tab-login.jpg)                   | ![screenshot](documentation/responsiveness/desktop/desk-login.png)                   | Works as expected |
| Reset password          | ![screenshot](documentation/responsiveness/mobile/mob-password-reset.jpg)          | ![screenshot](documentation/responsiveness/tablet/tab-password-reset.jpg)          | ![screenshot](documentation/responsiveness/desktop/desk-password-reset.png)          | Works as expected |
| Reset password done     | ![screenshot](documentation/responsiveness/mobile/mob-password-reset-done.jpg)     | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-done.jpg)     | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-done.png)     | Works as expected |
| Reset password key      | ![screenshot](documentation/responsiveness/mobile/mob-password-reset-key.jpg)      | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-key.jpg)      | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-key.png)      | Works as expected |
| Reset password key done | ![screenshot](documentation/responsiveness/mobile/mob-password-reset-key-done.jpg) | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-key-done.jpg) | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-key-done.png) | Works as expected |
| Home                    | ![screenshot](documentation/responsiveness/mobile/mob-home.jpg)                    | ![screenshot](documentation/responsiveness/tablet/tab-home.jpg)                    | ![screenshot](documentation/responsiveness/desktop/desk-home.png)                    | Works as expected |
| Contact                 | ![screenshot](documentation/responsiveness/mobile/mob-contact.jpg)                 | ![screenshot](documentation/responsiveness/tablet/tab-contact.jpg)                 | ![screenshot](documentation/responsiveness/desktop/desk-contact.png)                 | Works as expected |
| Logout                  | ![screenshot](documentation/responsiveness/mobile/mob-signout.jpg)                 | ![screenshot](documentation/responsiveness/tablet/tab-logout.jpg)                  | ![screenshot](documentation/responsiveness/desktop/desk-logout.png)                  | Works as expected |
| Listings                | ![screenshot](documentation/responsiveness/mobile/mob-list.jpg)                    | ![screenshot](documentation/responsiveness/tablet/tab-list.jpg)                    | ![screenshot](documentation/responsiveness/desktop/desk-list.png)                    | Works as expected |
| Add caravan             | ![screenshot](documentation/responsiveness/mobile/mob-add-caravan.jpg)             | ![screenshot](documentation/responsiveness/tablet/tab-add_caravan.jpg)             | ![screenshot](documentation/responsiveness/desktop/desk-add-caravan.png)             | Works as expected |
| Bookings                | ![screenshot](documentation/responsiveness/mobile/mob-book.jpg)                    | ![screenshot](documentation/responsiveness/tablet/tab-book.jpg)                    | ![screenshot](documentation/responsiveness/desktop/desk-book.png)                    | Works as expected |
| Account settings        | ![screenshot](documentation/responsiveness/mobile/mob-account.jpg)                 | ![screenshot](documentation/responsiveness/tablet/tab-account.jpg)                 | ![screenshot](documentation/responsiveness/desktop/desk-account.png)                 | Works as expected |
| 404                     | ![screenshot](documentation/responsiveness/mobile/mob-404.jpg)                     | ![screenshot](documentation/responsiveness/tablet/tab-404.jpg)                     | ![screenshot](documentation/responsiveness/desktop/desk-404.png)                     | Works as expected |
| 500                     | ![screenshot](documentation/responsiveness/mobile/mob-500.jpg)                     | ![screenshot](documentation/responsiveness/tablet/tab-500.jpg)                     | ![screenshot](documentation/responsiveness/desktop/desk-500.png)                     | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page                    | Chrome                                                                               | Firefox                                                                       | silk                                                                               | Notes             |
| ----------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Register                | ![screenshot](documentation/responsiveness/desktop/desk-register.png)                | ![screenshot](documentation/browsers/firefox/fox-login.png)                   | ![screenshot](documentation/responsiveness/tablet/tab-register.jpg)                | Works as expected |
| Login                   | ![screenshot](documentation/responsiveness/desktop/desk-login.png)                   | ![screenshot](documentation/browsers/firefox/fox-login.png)                   | ![screenshot](documentation/responsiveness/tablet/tab-login.jpg)                   | Works as expected |
| Logout                  | ![screenshot](documentation/responsiveness/desktop/desk-logout.png)                  | ![screenshot](documentation/browsers/firefox/fox-logout.png)                  | ![screenshot](documentation/responsiveness/tablet/tab-logout.jpg)                  | Works as expected |
| Home                    | ![screenshot](documentation/responsiveness/desktop/desk-home.png)                    | ![screenshot](documentation/browsers/firefox/fox-home.png)                    | ![screenshot](documentation/responsiveness/tablet/tab-home.jpg)                    | Works as expected |
| Add caravan             | ![screenshot](documentation/responsiveness/desktop/desk-add-caravan.png)             | ![screenshot](documentation/browsers/firefox/fox-add-caravan.png)             | ![screenshot](documentation/responsiveness/tablet/tab-add_caravan.jpg)             | Works as expected |
| Contact                 | ![screenshot](documentation/responsiveness/desktop/desk-contact.png)                 | ![screenshot](documentation/browsers/firefox/fox-contact.png)                 | ![screenshot](documentation/responsiveness/tablet/tab-contact.jpg)                 | Works as expected |
| Listings                | ![screenshot](documentation/responsiveness/desktop/desk-list.png)                    | ![screenshot](documentation/browsers/firefox/fox-list.png)                    | ![screenshot](documentation/responsiveness/tablet/tab-list.jpg)                    | Works as expected |
| Booking                 | ![screenshot](documentation/responsiveness/desktop/desk-book.png)                    | ![screenshot](documentation/browsers/firefox/fox-book.png)                    | ![screenshot](documentation/responsiveness/tablet/tab-list.jpg)                    | Works as expected |
| Account settings        | ![screenshot](documentation/responsiveness/desktop/desk-account.png)                 | ![screenshot](documentation/browsers/firefox/fox-account.png)                 | ![screenshot](documentation/responsiveness/tablet/tab-account.jpg)                 | Works as expected |
| Password reset          | ![screenshot](documentation/responsiveness/desktop/desk-password-reset.png)          | ![screenshot](documentation/browsers/firefox/fox-password-reset.png)          | ![screenshot](documentation/responsiveness/tablet/tab-password-reset.jpg)          | Works as expected |
| Password reset done     | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-done.png)     | ![screenshot](documentation/browsers/firefox/fox-password-reset-done.png)     | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-done.jpg)     | Works as expected |
| Password reset key      | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-key.png)      | ![screenshot](documentation/browsers/firefox/fox-password-reset-key.png)      | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-key.jpg)      | Works as expected |
| Password reset key done | ![screenshot](documentation/responsiveness/desktop/desk-password-reset-key-done.png) | ![screenshot](documentation/browsers/firefox/fox-password-reset-key-done.png) | ![screenshot](documentation/responsiveness/tablet/tab-password-reset-key-done.jpg) | Works as expected |
| 500                     | ![screenshot](documentation/responsiveness/desktop/desk-500.png)                     | ![screenshot](documentation/browsers/firefox/fox-500.png)                     | ![screenshot](documentation/responsiveness/tablet/tab-500.jpg)                     | Works as expected |
| 404                     | ![screenshot](documentation/responsiveness/desktop/desk-404.png)                     | ![screenshot](documentation/browsers/firefox/fox-404.png)                     | ![screenshot](documentation/responsiveness/tablet/tab-404.jpg)                     | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both _mobile_ and _desktop_.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page                    | Mobile                                                                               | Desktop                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Register                | ![screenshot](documentation/lighthouse/mobile/mob-register-light.png)                | ![screenshot](documentation/lighthouse/desktop/desk-register-light.png)                |
| Login                   | ![screenshot](documentation/lighthouse/mobile/mob-login-light.png)                   | ![screenshot](documentation/lighthouse/desktop/desk-login-light.png)                   |
| Home                    | ![screenshot](documentation/lighthouse/mobile/mob-home-light.png)                    | ![screenshot](documentation/lighthouse/desktop/desk-home-light.png)                    |
| Logout                  | ![screenshot](documentation/lighthouse/mobile/mob-logout-light.png)                  | ![screenshot](documentation/lighthouse/desktop/desk-logout-light.png)                  |
| Password reset          | ![screenshot](documentation/lighthouse/mobile/mob-password-reset-light.png)          | ![screenshot](documentation/lighthouse/desktop/desk-password-reset-light.png)          |
| Password reset done     | ![screenshot](documentation/lighthouse/mobile/mob-password-reset-done-light.png)     | ![screenshot](documentation/lighthouse/desktop/desk-pasword-reset-done-light.png)      |
| Password reset key      | ![screenshot](documentation/lighthouse/mobile/mob-password-reset-key-light.png)      | ![screenshot](documentation/lighthouse/desktop/desk-password-reset-key-light.png)      |
| Password reset key done | ![screenshot](documentation/lighthouse/mobile/mob-password-reset-key-done-light.png) | ![screenshot](documentation/lighthouse/desktop/desk-password-reset-key-done-light.png) |
| Contact                 | ![screenshot](documentation/lighthouse/mobile/mob-contact-light.png)                 | ![screenshot](documentation/lighthouse/desktop/desk-contact-light.png)                 |
| Dashboard               | ![screenshot](documentation/lighthouse/mobile/mob-dash-light.png)                    | ![screenshot](documentation/lighthouse/desktop/desk-dash-light.png)                    |
| Listings                | ![screenshot](documentation/lighthouse/mobile/mob-list-light.png)                    | ![screenshot](documentation/lighthouse/desktop/desk-list-light.png)                    |
| Add caravan             | ![screenshot](documentation/lighthouse/mobile/mob-add-caravan-light.png)             | ![screenshot](documentation/lighthouse/desktop/desk-add-caravan-light.png)             |
| Bookings                | ![screenshot](documentation/lighthouse/mobile/mob-book-light.png)                    | ![screenshot](documentation/lighthouse/desktop/desk-book-light.png)                    |
| Account settings        | ![screenshot](documentation/lighthouse/mobile/mob-account-light.png)                 | ![screenshot](documentation/lighthouse/desktop/desk-account-light.png)                 |
| 500                     | ![screenshot](documentation/lighthouse/mobile/mob-500-light.png)                     | ![screenshot](documentation/lighthouse/desktop/desk-500-light.png)                     |
| 404                     | ![screenshot](documentation/lighthouse/mobile/mob-404-light.png)                     | ![screenshot](documentation/lighthouse/desktop/desk-404-light.png)                     |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page                | Expectation                                                                                                | Test                                                                                | Result                                                                          | Screenshot                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Blog Management     | Feature is expected to allow the blog owner to create new posts with a title, featured image, and content. | Created a new post with valid title, image, and content data.                       | Post was created successfully and displayed correctly in the blog.              | ![screenshot](documentation/defensive/create-post.png)          |
|                     | Feature is expected to allow the blog owner to update existing posts.                                      | Edited the content of an existing blog post.                                        | Post was updated successfully with the new content.                             | ![screenshot](documentation/defensive/update-post.png)          |
|                     | Feature is expected to allow the blog owner to delete blog posts.                                          | Attempted to delete a blog post, confirming the action before proceeding.           | Blog post was deleted successfully.                                             | ![screenshot](documentation/defensive/delete-post.png)          |
|                     | Feature is expected to retrieve a list of all published posts.                                             | Accessed the blog owner dashboard to view all published posts.                      | All published posts were displayed in a list view.                              | ![screenshot](documentation/defensive/published-posts.png)      |
|                     | Feature is expected to preview posts as drafts before publishing.                                          | Created a draft post and previewed it.                                              | Draft was displayed correctly in preview mode.                                  | ![screenshot](documentation/defensive/preview-draft.png)        |
| Comments Management | Feature is expected to allow the blog owner to approve or reject comments.                                 | Approved and rejected comments from the dashboard.                                  | Approved comments were published; rejected comments were removed.               | ![screenshot](documentation/defensive/review-comments.png)      |
|                     | Feature is expected to allow the blog owner to edit or delete comments.                                    | Edited and deleted existing comments.                                               | Comments were updated or removed successfully.                                  | ![screenshot](documentation/defensive/edit-delete-comments.png) |
| User Authentication | Feature is expected to allow registered users to log in to the site.                                       | Attempted to log in with valid and invalid credentials.                             | Login was successful with valid credentials; invalid credentials were rejected. | ![screenshot](documentation/defensive/login.png)                |
|                     | Feature is expected to allow users to register for an account.                                             | Registered a new user with unique credentials.                                      | User account was created successfully.                                          | ![screenshot](documentation/defensive/register.png)             |
|                     | Feature is expected to allow users to log out securely.                                                    | Logged out and tried accessing a restricted page.                                   | Access was denied after logout, as expected.                                    | ![screenshot](documentation/defensive/logout.png)               |
| User Comments       | Feature is expected to allow registered users to leave comments on blog posts.                             | Logged in and added comments to a blog post.                                        | Comments were successfully added and marked as pending approval.                | ![screenshot](documentation/defensive/add-comment.png)          |
|                     | Feature is expected to display a notification that comments are pending approval.                          | Added a comment and checked the notification message.                               | Notification was displayed as expected.                                         | ![screenshot](documentation/defensive/pending-approval.png)     |
|                     | Feature is expected to allow users to edit their own comments.                                             | Edited personal comments.                                                           | Comments were updated as expected.                                              | ![screenshot](documentation/defensive/edit-user-comments.png)   |
|                     | Feature is expected to allow users to delete their own comments.                                           | Deleted personal comments.                                                          | Comments were removed as expected.                                              | ![screenshot](documentation/defensive/delete-user-comments.png) |
| Guest Features      | Feature is expected to allow guest users to read blog posts without registering.                           | Opened blog posts as a guest user.                                                  | Blog posts were fully accessible without logging in.                            | ![screenshot](documentation/defensive/view-posts-guest.png)     |
|                     | Feature is expected to display the names of other commenters on posts.                                     | Checked the names of commenters on posts as a guest user.                           | Commenter names were displayed as expected.                                     | ![screenshot](documentation/defensive/commenter-names.png)      |
|                     | Feature is expected to block standard users from brute-forcing admin pages.                                | Attempted to navigate to admin-only pages by manipulating the URL (e.g., `/admin`). | Access was blocked, and a message was displayed showing denied access.          | ![screenshot](documentation/defensive/brute-force.png)          |
| 404 Error Page      | Feature is expected to display a 404 error page for non-existent pages.                                    | Navigated to an invalid URL (e.g., `/test`).                                        | A custom 404 error page was displayed as expected.                              | ![screenshot](documentation/defensive/404.png)                  |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target               | Expectation                                                                             | Outcome                                                                             | Screenshot                                          |
| -------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------- |
| As a blog owner      | I would like to create new blog posts with a title, featured image, and content         | so that I can share my experiences with my audience.                                | ![screenshot](documentation/features/feature01.png) |
| As a blog owner      | I would like to update existing blog posts                                              | so that I can correct or add new information to my previous stories.                | ![screenshot](documentation/features/feature02.png) |
| As a blog owner      | I would like to delete blog posts                                                       | so that I can remove outdated or irrelevant content from my blog.                   | ![screenshot](documentation/features/feature03.png) |
| As a blog owner      | I would like to retrieve a list of all my published blog posts                          | so that I can manage them from a central dashboard.                                 | ![screenshot](documentation/features/feature04.png) |
| As a blog owner      | I would like to preview a post as draft before publishing it                            | so that I can ensure formatting and content appear correctly.                       | ![screenshot](documentation/features/feature05.png) |
| As a blog owner      | I would like to review comments before they are published                               | so that I can filter out spam or inappropriate content.                             | ![screenshot](documentation/features/feature06.png) |
| As a blog owner      | I would like to approve or reject comments from users                                   | so that I can maintain control over the discussion on my posts.                     | ![screenshot](documentation/features/feature07.png) |
| As a blog owner      | I would like to view a list of all comments (both approved and pending)                 | so that I can manage user engagement effectively.                                   | ![screenshot](documentation/features/feature08.png) |
| As a blog owner      | I would like to edit or delete user comments                                            | so that I can clean up or remove inappropriate responses after they've been posted. | ![screenshot](documentation/features/feature09.png) |
| As a registered user | I would like to log in to the site                                                      | so that I can leave comments on blog posts.                                         | ![screenshot](documentation/features/feature10.png) |
| As a registered user | I would like to register for an account                                                 | so that I can become part of the community and engage with the blog.                | ![screenshot](documentation/features/feature11.png) |
| As a registered user | I would like to leave a comment on a blog post                                          | so that I can share my thoughts or ask questions about the owner's experiences.     | ![screenshot](documentation/features/feature12.png) |
| As a registered user | I would like my comment to show my name and the timestamp                               | so that others can see who I am and when I left the comment.                        | ![screenshot](documentation/features/feature13.png) |
| As a registered user | I would like to receive a notification or message saying my comment is pending approval | so that I understand it hasn't been posted immediately.                             | ![screenshot](documentation/features/feature14.png) |
| As a registered user | I would like to edit or delete my own comments                                          | so that I can fix mistakes or retract my statement.                                 | ![screenshot](documentation/features/feature15.png) |
| As a guest user      | I would like to read blog posts without registering                                     | so that I can enjoy the content without needing to log in.                          | ![screenshot](documentation/features/feature16.png) |
| As a guest user      | I would like to browse past posts                                                       | so that I can explore the blog's full content history.                              | ![screenshot](documentation/features/feature17.png) |
| As a guest user      | I would like to register for an account                                                 | so that I can participate in the community by leaving comments on posts.            | ![screenshot](documentation/features/feature18.png) |
| As a guest user      | I would like to see the names of other commenters on posts                              | so that I can get a sense of community interaction before registering.              | ![screenshot](documentation/features/feature19.png) |
| As a user            | I would like to see a 404 error page if I get lost                                      | so that it's obvious that I've stumbled upon a page that doesn't exist.             | ![screenshot](documentation/features/feature20.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Jest procedures, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality. In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `<enter>` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work. Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test. The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the very bottom of the file. Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially. Write JS code that can get the tests to pass as part of the Red-Green refactor process. Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests     | Screenshot                                                |
| ----------- | --------- | --------------------------------------------------------- |
| 1 passed    | 16 passed | ![screenshot](documentation/automation/jest-coverage.png) |

#### Jest Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Jest tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with Jest.

⚠️ --- END --- ⚠️

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/AshLaw96/Nomad-Nation/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AAshLaw96%2FNomad-Nation%20label%3Abug&label=bugs)](https://www.github.com/AshLaw96/Nomad-Nation/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/AshLaw96/Nomad-Nation/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/AshLaw96/Nomad-Nation/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation/issues)

Any remaining open issues can be tracked [here](https://www.github.com/AshLaw96/Nomad-Nation/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue                                                                                                                             | Screenshot                                             |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling.                                         | ![screenshot](documentation/issues/overflow.png)       |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package.                                                        | ![screenshot](documentation/issues/allauth.png)        |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

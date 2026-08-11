\# Playwright Automation Skill



\## Purpose



Generate and maintain enterprise-grade UI automation frameworks using Playwright and Python.



The generated automation solution must be scalable, maintainable, reusable, and aligned with industry-standard test automation practices.



\---



\# Technology Stack



\* Language: Python

\* Automation Framework: Playwright

\* Test Runner: Pytest

\* Design Pattern: Page Object Model (POM)



\---



\# Core Principles



1\. Follow Page Object Model (POM) architecture.

2\. Prioritize code reusability and maintainability.

3\. Avoid duplicate code, locators, and utility methods.

4\. Generate clean, readable, and self-documenting code.

5\. Ensure all automation components are modular and reusable.

6\. Follow consistent naming conventions across the framework.



\---



\# Project Structure Standards



Maintain clear separation of responsibilities.



```text

PageObjects/

Locators/

Utilities/

TestCases/

TestData/

Reports/

Logs/

```



\## Mandatory Rules



\* Page objects must contain page-specific actions only.

\* Locators must be stored in dedicated page-specific locator files.

\* Test cases must contain business flow validation only.

\* Utility functions must be centralized and reusable.

\* Never mix locators, page actions, test logic, and utility methods in the same file.



\---



\# Locator Strategy Standards



Use the most stable and maintainable locator strategy available.



\## Preferred Locator Priority



1\. getByRole()

2\. getByLabel()

3\. getByPlaceholder()

4\. getByText()

5\. getByTestId()

6\. XPath

7\. CSS Selector (last resort only)



\## Locator Rules



\* Every locator must uniquely identify a single element.

\* Avoid fragile or dynamic locators.

\* Avoid absolute XPath expressions.

\* Use CSS selectors only when no reliable alternative exists.

\* Validate locator uniqueness before implementation.

\* Locator names must clearly describe the element being identified.



\### Examples



Good:



```python

login\_button

username\_input\_field

submit\_payment\_button

```



Avoid:



```python

btn1

input1

element

```



\---



\# Page Object Standards



Each page must have:



\* Dedicated Page Object file

\* Dedicated Locator file

\* Page-specific actions only



Example:



```text

PageObjects/

&#x20;   LoginPage.py



Locators/

&#x20;   LoginPageLocators.py

```



\---



\# Reusability Standards



Before creating any new:



\* Locator

\* Method

\* Utility

\* Page Object



Always check whether an equivalent implementation already exists.



\## Rules



\* Reuse existing framework components whenever possible.

\* Do not create duplicate wrappers.

\* Do not duplicate business actions across page objects.

\* Consolidate common functionality into reusable utility methods.



\---



\# Wrapper Method Standards



Common interactions must be implemented through reusable wrappers.



Examples:



```python

click\_element()

enter\_text()

clear\_text()

get\_text()

wait\_for\_element()

wait\_for\_page\_load()

select\_dropdown\_value()

verify\_element\_visible()

```



Direct interaction with Playwright APIs should be minimized when reusable wrappers already exist.



\---



\# Naming Convention Standards



\## Class Names



Use descriptive PascalCase names.



Examples:



```python

LoginPage

UserRegistrationPage

PaymentConfirmationPage

```



\## Method Names



Use descriptive action-oriented names.



Examples:



```python

enter\_username()

click\_login\_button()

verify\_success\_message\_displayed()

```



\## Variable Names



Use meaningful snake\_case names.



Examples:



```python

username\_input\_field

payment\_submit\_button

customer\_account\_number

```



\---



\# Documentation Standards



Every class and method must include meaningful docstrings.



\## Class Example



```python

class LoginPage:

&#x20;   """

&#x20;   Handles all user interactions and validations

&#x20;   related to the application login page.

&#x20;   """

```



\## Method Example



```python

def enter\_username(self, username: str):

&#x20;   """

&#x20;   Enter the username into the login input field.



&#x20;   Args:

&#x20;       username: Valid application username.

&#x20;   """

```



\---



\# Wait Strategy Standards



\## Mandatory Rules



\* Use explicit waits.

\* Avoid hardcoded waits.

\* Avoid time.sleep().

\* Wait for expected application state before interaction.



Preferred:



```python

locator.wait\_for()

```



Avoid:



```python

time.sleep(5)

```



\---



\# Test Case Design Standards



\* One test should validate one business objective.

\* Keep tests independent.

\* Avoid interdependent test execution.

\* Ensure tests are repeatable and deterministic.

\* Use meaningful test names.



Example:



```python

test\_user\_can\_login\_with\_valid\_credentials()

```



\---



\# Quality Validation Checklist



Before generating or modifying automation code, validate:



✓ POM pattern followed

✓ No duplicate locators

✓ No duplicate utility methods

✓ Locator uniqueness verified

✓ Descriptive naming conventions followed

✓ Reusable wrappers utilized

✓ Proper docstrings added

✓ No hardcoded waits

✓ No unnecessary code duplication

✓ Framework structure maintained



\---



\# Expected Outcome



Generate automation code that is:



\* Readable

\* Maintainable

\* Reusable

\* Scalable

\* Enterprise-ready

\* Easy to debug

\* Easy to extend

\* Aligned with Playwright and Python best practices




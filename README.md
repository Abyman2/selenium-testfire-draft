# Selenium E2E Automation Project

This project contains a Java + Maven + Selenium suite built against a public, stable demo shop:
Practice Software Testing - Toolshop.

## Project summary

Website used:
- https://practicesoftwaretesting.com/
- Login page: https://practicesoftwaretesting.com/auth/login

This site was chosen because it has:
- a visible login form,
- a clear positive user flow after login,
- an invalid-login path with validation feedback,
- a public demo environment suitable for browser automation.

## Requirements

- Java 17+
- Maven 3.8+
- Google Chrome installed
- Internet connection for the first driver setup and test execution

## Run the suite

```bash
mvn test
```

The suite is configured to run headless by default unless the browser is explicitly opened in non-headless mode.

## Project structure

```text
src/main/java/pages/
  LoginPage.java
  AccountSummaryPage.java

src/test/java/base/
  BaseTest.java

src/test/java/tests/
  NavigationSmokeTest.java
  LoginTest.java
  LoginParameterizedTest.java

pom.xml
README.md
```

## Test coverage

- T1: navigation smoke test
- T2: at least two locator strategies used across the suite
- T3: positive login flow with success assertions
- T4: negative login flow with invalid-message assertions
- T5: WebDriverWait + ExpectedConditions used for dynamic waits
- T6: parameterized invalid-input test using equivalence partitioning
- T7: page objects used instead of raw locator calls in tests

## Valid login credentials used

- Email: admin@practicesoftwaretesting.com
- Password: welcome01

## Notes

- No Thread.sleep is used anywhere.
- The suite uses explicit waits and page-object methods.
- The project now reflects the live working site rather than the outdated Altoro demo assumptions.

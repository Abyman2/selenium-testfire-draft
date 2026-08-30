# Selenium E2E Tests — Altoro Mutual (demo.testfire.net)

Automated end-to-end tests for [https://demo.testfire.net](https://demo.testfire.net) ("Altoro
Mutual"), a banking demo site built for security/QA practice, with an on-homepage login box,
a post-login account summary page, and clear pass/fail signals — built for the Software Testing
and Validation Selenium homework.

## Requirements

- Java 17+
- Maven 3.8+
- Google Chrome installed (WebDriverManager downloads the matching chromedriver automatically —
  no manual driver setup, but it does need an internet connection the first time it runs)

## Running the suite

```bash
mvn test
```

Runs headless by default. To watch the browser instead:

```bash
mvn test -Dheadless=false
```

## Project structure

```
src/main/java/pages/        Page Objects (LoginPage, AccountSummaryPage)
src/test/java/base/         Shared JUnit lifecycle (BaseTest: @BeforeEach/@AfterEach)
src/test/java/tests/        Test classes
  NavigationSmokeTest.java       T1 — smoke test
  LoginTest.java                 T3 — positive path, T4 — negative path
  LoginParameterizedTest.java    T6 — data-driven test (equivalence partitioning on credentials)
```

Two locator strategies (T2) are used across the Page Objects: `By.name` for the sign-in box
fields (Altoro Mutual's markup gives these stable `name` attributes but no ids), and
non-positional `By.xpath` (built on visible text) for the "Login Failed" message and the
"Account Summary" heading, plus `By.linkText` for the Logout link.

## Important: verify before you submit

I wrote and reviewed this code carefully, but **I built it without live internet access**, so I
could not actually load demo.testfire.net, inspect its current DOM, or run `mvn test` myself in
this environment. The credentials and locators below are based on this site's well-documented,
long-standing structure (it's a stable IBM-maintained practice site, largely unchanged for years),
but you should still verify before submitting:

- Demo login: `admin` / `admin` — this is the standard published credential pair for this site.
- `name="uid"`, `name="passw"` (the sign-in box fields), `input[value='Login']` (submit button).
- Text match on "Login Failed" for the error case, and on "Account Summary" for the post-login
  heading.

**Before you submit:** run `mvn test -Dheadless=false` once so you can watch it. If a locator or
the demo credentials don't match (site copy does change occasionally), right-click that spot on
the real page → Inspect, and update the matching `By.*` or credential in `LoginTest` /
`LoginParameterizedTest` / the Page Objects. That's normal Selenium maintenance, not a sign
something is broken. Note anything you had to change in your report's "defects or odd behaviour"
section — that's exactly the kind of observation the report asks for.

## Notes

- No `Thread.sleep` anywhere — waits use `WebDriverWait` + `ExpectedConditions`.
- The suite is polite to the target site: each test does exactly one login attempt, nothing
  looped.

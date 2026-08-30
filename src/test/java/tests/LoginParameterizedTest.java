package tests;

import base.BaseTest;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import pages.LoginPage;

import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * T6: a parameterized test using equivalence partitioning for invalid login inputs.
 */
class LoginParameterizedTest extends BaseTest {

    @ParameterizedTest(name = "[{index}] email={0} password={1} -> invalid login")
    @CsvSource({
            "admin@practicesoftwaretesting.com, wrongpass",
            "unknown@example.com, welcome01",
            "'', welcome01",
            "admin@practicesoftwaretesting.com, ''"
    })
    void invalidCredentialPartitionsShowLoginFailed(String email, String password) {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.openLoginPage(BASE_URL);
        loginPage.login(email, password);

        if (email == null || email.isBlank() || password == null || password.isBlank()) {
            assertTrue(driver.getCurrentUrl().contains("/auth/login"),
                    "Blank fields should trigger form validation and keep the user on the login page. "
                            + "Current URL: " + driver.getCurrentUrl());
            assertTrue(loginPage.isLoginFormDisplayed(),
                    "Login form should remain visible when required fields are empty.");
            return;
        }

        String error = loginPage.getLoginFailedMessage();
        assertTrue(error.toLowerCase().contains("invalid email or password"),
                "Expected an invalid-login message for email=[" + email + "] password=[" + password
                        + "] but got: " + error);
    }
}

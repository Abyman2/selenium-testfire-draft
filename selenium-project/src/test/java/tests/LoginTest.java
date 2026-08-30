package tests;

import base.BaseTest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import pages.AccountSummaryPage;
import pages.LoginPage;

import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * T3 positive flow and T4 negative flow.
 */
class LoginTest extends BaseTest {

    private static final String VALID_EMAIL = "admin@practicesoftwaretesting.com";
    private static final String VALID_PASSWORD = "welcome01";

    @Test
    @DisplayName("T3: valid login reaches the dashboard")
    void validLoginReachesAccountSummary() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.openLoginPage(BASE_URL);
        loginPage.login(VALID_EMAIL, VALID_PASSWORD);

        AccountSummaryPage summaryPage = new AccountSummaryPage(driver);
        assertTrue(summaryPage.waitUntilLoaded(), "Dashboard content should appear after valid login");
        assertTrue(summaryPage.isSignOutLinkDisplayed(), "Sign out should be visible once logged in");
    }

    @Test
    @DisplayName("T4: wrong password shows invalid credentials error")
    void invalidPasswordShowsLoginFailed() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.openLoginPage(BASE_URL);
        loginPage.login(VALID_EMAIL, "wrong_password");

        String error = loginPage.getLoginFailedMessage();
        assertTrue(error.toLowerCase().contains("invalid email or password"),
                "Expected the invalid-login message but got: " + error);
    }
}

package tests;

import base.BaseTest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import pages.LoginPage;

import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * T1: smoke test proving the application loaded.
 */
class NavigationSmokeTest extends BaseTest {

    @Test
    @DisplayName("T1: home page loads with the expected title and login form")
    void homePageLoads() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.open(BASE_URL);

        assertTrue(loginPage.getTitle().contains("Practice Software Testing"),
                "Page title should confirm the app loaded, but was: " + loginPage.getTitle());
        assertTrue(loginPage.isSignInLinkDisplayed(), "Sign in link should be visible on the home page");
    }
}

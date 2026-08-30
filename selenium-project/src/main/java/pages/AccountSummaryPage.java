package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

/**
 * Page Object for the post-login dashboard page.
 */
public class AccountSummaryPage {

    private final WebDriver driver;
    private final WebDriverWait wait;

    private final By dashboardHeading = By.xpath("//*[contains(text(),'Sales over the years')]");
    private final By signOutLink = By.xpath("//*[contains(text(),'Sign out')]");

    public AccountSummaryPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    // T5: explicit wait for the dashboard content after login.
    public boolean waitUntilLoaded() {
        WebElement heading = wait.until(ExpectedConditions.visibilityOfElementLocated(dashboardHeading));
        return heading.isDisplayed();
    }

    public boolean isSignOutLinkDisplayed() {
        return !driver.findElements(signOutLink).isEmpty();
    }
}

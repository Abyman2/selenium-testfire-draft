package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

/**
 * Page Object for the Practice Software Testing login page.
 */
public class LoginPage {

    private final WebDriver driver;
    private final WebDriverWait wait;

    // T2: at least two locator strategies are used here.
    private final By emailField = By.id("email");
    private final By passwordField = By.id("password");
    private final By loginButton = By.cssSelector("input[type='submit']");
    private final By loginError = By.xpath("//*[contains(text(),'Invalid email or password')]");
    private final By signInLink = By.linkText("Sign in");

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void open(String baseUrl) {
        driver.get(baseUrl);
    }

    public void openLoginPage(String baseUrl) {
        driver.get(baseUrl + "auth/login");
    }

    public String getTitle() {
        return driver.getTitle();
    }

    public boolean isLoginFormDisplayed() {
        WebElement email = wait.until(ExpectedConditions.visibilityOfElementLocated(emailField));
        return email.isDisplayed();
    }

    public boolean isSignInLinkDisplayed() {
        return wait.until(ExpectedConditions.visibilityOfElementLocated(signInLink)).isDisplayed();
    }

    public void login(String email, String password) {
        WebElement emailInput = wait.until(ExpectedConditions.visibilityOfElementLocated(emailField));
        WebElement passwordInput = wait.until(ExpectedConditions.visibilityOfElementLocated(passwordField));
        emailInput.clear();
        emailInput.sendKeys(email);
        passwordInput.clear();
        passwordInput.sendKeys(password);
        wait.until(ExpectedConditions.elementToBeClickable(loginButton)).click();
    }

    // T5: explicit wait on the error element instead of Thread.sleep.
    public String getLoginFailedMessage() {
        WebElement error = wait.until(ExpectedConditions.visibilityOfElementLocated(loginError));
        return error.getText();
    }
}

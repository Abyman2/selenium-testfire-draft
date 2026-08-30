import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Check {
  public static void main(String[] args) {
    WebDriverManager.chromedriver().setup();
    ChromeOptions options = new ChromeOptions();
    options.setAcceptInsecureCerts(true);
    options.addArguments("--headless=new");
    options.addArguments("--ignore-certificate-errors");
    options.addArguments("--allow-insecure-localhost");
    options.addArguments("--window-size=1400,1000");
    options.addArguments("--disable-gpu");
    options.addArguments("--no-sandbox");
    WebDriver driver = new ChromeDriver(options);
    driver.get("https://demo.testfire.net/");
    System.out.println("URL=" + driver.getCurrentUrl());
    System.out.println("TITLE=" + driver.getTitle());
    String src = driver.getPageSource();
    System.out.println(src.substring(0, 800));
    driver.quit();
  }
}

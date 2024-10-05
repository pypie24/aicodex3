package hellocucumber;

import io.cucumber.java.en.*;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.*;

public class StepDefinitions {

    public static WebDriver driver;

    @Given("the user is on the login page")
    public void theUserIsOnTheLoginPage() throws InterruptedException {
        driver = new ChromeDriver();
        driver.get("http://localhost:3000/");
        Thread.sleep(5000);
    }

    @When("the user enters valid credentials")
    public void theUserEntersValidCredentials() {
        driver.findElement(By.xpath("//*[@name='username']")).sendKeys("Admin");
        driver.findElement(By.xpath("//*[@name='password']")).sendKeys("admin123");
        driver.findElement(By.xpath("//button[contains(.,'Login')]")).click();

    }

    @Then("the user is redirected to the dashboard")
    public void theUserIsRedirectedToTheDashboard() {
        String currenturl = driver.getCurrentUrl();
        Assertions.assertEquals(currenturl,"https://vnexpress.net/");

    }

    @When("the user enters {string} and {string}")
    public void theUserEntersAnd(String username, String password) {
        driver.findElement(By.xpath("//*[@name='username']")).sendKeys(username);
        driver.findElement(By.xpath("//*[@name='password']")).sendKeys(password);
        driver.findElement(By.xpath("//button[contains(.,'Login')]")).click();
    }

    @AfterAll
    public static void teardownmethod()
    {
        driver.quit();
    }
}

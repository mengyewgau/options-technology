import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class StockApp extends Application {

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Stock Option Finder");

        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        Label stockPriceLabel = new Label("Stock Price:");
        grid.add(stockPriceLabel, 0, 1);

        TextField stockPriceTextField = new TextField();
        grid.add(stockPriceTextField, 1, 1);

        Button btn = new Button("Send");
        grid.add(btn, 1, 2);

        Label responseLabel = new Label();
        grid.add(responseLabel, 1, 3);

        btn.setOnAction(e -> {
            String stockPrice = stockPriceTextField.getText();
            String response = sendStockPrice(stockPrice);
            responseLabel.setText("Response: " + response);
        });

        Scene scene = new Scene(grid, 300, 275);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private String sendStockPrice(String stockPrice) {
        // Dummy function to simulate API call
        // Replace with actual HTTP call code
        return "Option Price: 100, Type: Call, Recommendation: Buy";
    }

    public static void main(String[] args) {
        launch(args);
    }
}

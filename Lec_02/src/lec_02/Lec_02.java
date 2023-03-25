/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lec_02;


import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.image.Image;
import javafx.scene.layout.StackPane;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;

/**
 *
 * @author Jonab
 */
public class Lec_02 extends Application {
    
    @Override
    public void start(Stage primaryStage) throws Exception {
//        Button btn = new Button();
//        btn.setText("Say 'Hello World'");
//        btn.setOnAction(new EventHandler<ActionEvent>() {
//            
//            @Override
//            public void handle(ActionEvent event) {
//                System.out.println("Hello World!");
//            }
//        });
//        //Group group = new Group();
//        StackPane root = new StackPane();
//        root.getChildren().add(btn);
//        
//        Scene scene = new Scene(root, 300, 250);
//        
//        primaryStage.setTitle("Hello World!");
//        primaryStage.setScene(scene);
//        primaryStage.show();
          Image image = new Image("https://cdn.britannica.com/85/13085-050-C2E88389/Corpus-Christi-College-University-of-Cambridge-England.jpg");
          ImageView imageView = new ImageView(image);
          imageView.setX(70); 
          imageView.setY(150);
          imageView.setFitHeight(200); //setting the fit height and width of the image view
          imageView.setFitWidth(200);
          imageView.setPreserveRatio(true) ;

          Rectangle rectangle = new Rectangle(); 
          rectangle.setX(120); //Setting the Properties of the Rectangle
          rectangle.setY(120);
          rectangle.setWidth(200);
          rectangle.setHeight(100);
          
          Circle circle = new Circle();
          circle.setCenterX(150); //Setting the Properties of the Circle
          circle.setCenterY(150);
          circle.setRadius(20);

          Line line = new Line(100 , 250 , 250 , 250 ) ;
          line.setFill(Color.DEEPPINK);
          
          Text text = new Text(50,50,"Once upon a time you were \na small child with BIG DREAMS \nthat you promised you'd make real \none day Don't disappoint yourselfe ");
          text.setFont(Font.font(STYLESHEET_CASPIAN,FontWeight.BOLD, FontPosture.REGULAR, 15));
          text.setFill(Color.DARKSEAGREEN);
         // text.setStroke(Color.BLACK);
          text.setStrokeWidth(2);
          //text.setUnderline(true);
          
          //text.setStrikethrough(true);
          //StackPane root_pane = new StackPane(text,line);
          
          Group group = new Group( imageView , text );
          Scene scene = new Scene(group,350,350);
          scene.setFill(Color.BEIGE);
          primaryStage.setTitle("Lec_02");
          primaryStage.setScene(scene);
          primaryStage.show();

     
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    
}

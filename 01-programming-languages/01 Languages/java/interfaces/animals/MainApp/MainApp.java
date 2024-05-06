// package MainApp;

public class MainApp {
    public static void main(String[] args) {
        System.out.println("----------------------------");
        System.out.println("Testing individual classe.");
        
        Dog dog = new Dog();
        dog.eat();
        dog.speak();

        Cow cow = new Cow();
        cow.eat();
        cow.speak();

        // OR using the Animal class
        Animal bird = new Bird();
        bird.eat();
        bird.speak();

        // Posterior, Array of anymals
        System.out.println("----------------------------");
        System.out.println("Testing array of animals, (diferent object classes)");
        Animal [] animals = {
            new Cow(),
            new Dog(),
            new Bird()
        };

        // for (Animal animal : animals){ // only for ArrayList
        for (int i = 0; i < animals.length; i++){
            animals[i].speak();
            animals[i].eat();
        }
    }
    
}
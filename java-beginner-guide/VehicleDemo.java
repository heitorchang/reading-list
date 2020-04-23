class Vehicle {
    int wheels;
    int passengers;
}

class VehicleDemo {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        v.wheels = 4;
        System.out.println(v.passengers);
    }
}

//Initializing pinout
int light_source = 6; //D6
int light_sensor = A1; //14
float data_sensor;
float voltage;
int i; //Value for PWM signal light_source

void setup() {
  //Declare baudrate
  Serial.begin(9600);
  //Declaring LED pin as output
  pinMode(light_source, OUTPUT);
  pinMode(light_sensor, INPUT);
}

void loop() {
  i = 255; //between 0-225 for PWM signal
  analogWrite(light_source, 115);
  data_sensor = analogRead(light_sensor);
  voltage = data_sensor * 5.0/1023;
  Serial.print("Data from sensor: ");
  Serial.println(voltage);
  delay(1000); //delay for 1 second
}

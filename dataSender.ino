void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}
int a = 0;
void loop() {
  // put your main code here, to run repeatedly:
a++;
ATR("sensor1",a);
a++;
ATR("Sensor2",a);
Serial.print("\n");//don't forget print \n to raspberry understand new line

}

void ATR(String s, int v){
  Serial.print("+");
Serial.print(s);
Serial.print("|");
 Serial.print(v);
 Serial.print("*");
}

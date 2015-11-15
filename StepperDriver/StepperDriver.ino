int xcoordinate = 0;
int ycoordinate = 0;
double baseAngle = 0;
double ArmAngle = 0;
int INPUT_SIZE = 40;

#include <AFMotor.h>

// Connect a stepper motor with 48 steps per revolution (7.5 degree)
// to motor port #2 (M3 and M4)
AF_Stepper motor(200, 2);
AF_Stepper motor1(200, 1);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");

  motor.setSpeed(80);  // 10 rpm   
  motor1.setSpeed(80);  // 10 rpm   

}

void forwardBase(int stepnum)
{
  motor.step(stepnum, FORWARD, MICROSTEP); 
}

void reverseBase(int stepnum)
{
  motor.step(stepnum, BACKWARD, MICROSTEP); 
}

void forwardLaser(int stepnum)
{
  motor1.step(stepnum, FORWARD, MICROSTEP); 
}

void reverseLaser(int stepnum)
{
  motor1.step(stepnum, BACKWARD, MICROSTEP); 
}


void parseSerial()
{

  // Get next command from Serial (add 1 for final 0)
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;

  // Read each command pair 
  char* command = strtok(input, "&");
  while (command != 0)
  {
    // Split the command in two values
    char* separator = strchr(command, ':');
    if (separator != 0)
    {
      // Actually split the string in 2: replace ':' with 0
      *separator = 0;
      xcoordinate = atoi(command);
      ++separator;
      ycoordinate = atoi(separator);

      // Do something with servoId and position
    }
    // Find the next command in input string
    command = strtok(0, "&");
  }
}

void loop() {
  parseSerial();
  if(xcoordinate > 0)
    forwardBase(xcoordinate);
  else if(xcoordinate < 0)
    reverseBase(abs(xcoordinate));
  if(ycoordinate > 0)
    forwardLaser(ycoordinate);
  else if(ycoordinate < 0)
    reverseLaser(abs(ycoordinate));
  xcoordinate = 0;
  ycoordinate = 0;
}




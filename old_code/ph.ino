/*
 # This sample code is used to test the pH meter V1.0.
 # Editor : Micah Weiss
 # Ver    : 1.0
 # Product: analog pH meter
 # SKU    : SEN0161
*/
#define SensorPin A0            //pH meter Analog output to Arduino Analog Input 0
#define TdsSensorPin A1
#define tempPin A2
#define VREF 5.0
#define SCOUNT 30    // size of the array
#define Offset 0.5            //deviation compensate. Test Ph against a solution with a know ph to determine offset. know solution ph 7, sensor says 6.88, offset is 0.12
#define samplingInterval 20
#define printInterval 800
#define ArrayLenth  40    //times of collection
int pHArray[ArrayLenth];   //Store the average value of the sensor feedback
int pHArrayIndex=0;
int analogBuffer[SCOUNT];
int analogBufferTemp[SCOUNT];
int analogBufferIndex = 0, copyIndex = 0;
int averageVoltage = 0, tdsValue = 0, temperature = 25; // when you prove that temp sensor works, change to temp
int temp = 0;

void setup(void)
{
  Serial.begin(9600);
  pinMode(SensorPin, INPUT);
  pinMode(TdsSensorPin, INPUT);
  pinMode(tempPin, INPUT);
}
void loop(void)
{
  static unsigned long samplingTime = millis(); // millis() returns the time since the program started *resets after 50 days
  static unsigned long printTime = millis();
 
  static float pHValue,voltage;
  if(millis()-samplingTime > samplingInterval) // operation to take a sample
  {
      #EC
      analogBuffer[analogBufferIndex] = analogRead(TdsSensorPin);
      analogBufferIndex++;
      if (analogBufferIndex == SCOUNT) analogBufferIndex = 0;
      #pH
      pHArray[pHArrayIndex++]=analogRead(SensorPin); // pHArrayIndex++ increases pHArrayIndex by one, subsequently increasing the size of the array
      if(pHArrayIndex==ArrayLenth)pHArrayIndex=0; // resets the pHArrayIndex when the max arraylength is reached
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      pHValue = 3.5*voltage+Offset;
      samplingTime=millis();
      #Temp
      temp = digitalRead(tempPin);
  }
  if(millis() - printTime > printInterval)   //Every 800 milliseconds, write a numerical, convert the state of the LED indicator
  {
    #EC
    for (copyIndex = 0; copyIndex < SCOUNT; copyIndex++)
      analogBufferTemp[copyIndex] = analogBuffer[copyIndex];
    averageVoltage = getMedianNum(analogBufferTemp, SCOUNT) * (float)VREF / 1024.0;
    float compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0);
    float compensationVoltage = averageVoltage / compensationCoefficient;
    tdsValue = (133.42 * compensationVoltage * compensationVoltage * compensationVoltage - 255.86 * compensationVoltage * compensationVoltage + 857.39 * compensationVoltage) * 0.5;
   
    #pH
    payload = str(voltage) + "#" str(pHValue) + "#" + str(tdsValue) + str(temp) + "\n"
    Serial.write(payload)
    #Serial.print("Voltage:");
    #   Serial.print(voltage,2); // print(foo, 2); the two specifies the number of values to print after the decimal
    #   Serial.print("#pH value:");
    #Serial.println(pHValue,2);
    #    digitalWrite(LED,digitalRead(LED)^1);
        printTime=millis();
  }
}
int getMedianNum(int bArray[], int iFilterLen)
{
  int bTab[iFilterLen];
  for (byte i = 0; i < iFilterLen; i++)
    bTab[i] = bArray[i];
  int i, j, bTemp;
  for (j = 0; j < iFilterLen - 1; j++)
  {
    for (i = 0; i < iFilterLen - j - 1; i++)
    {
      if (bTab[i] > bTab[i + 1])
      {
        bTemp = bTab[i];
        bTab[i] = bTab[i + 1];
        bTab[i + 1] = bTemp;
      }
    }
  }
  if ((iFilterLen & 1) > 0)
    bTemp = bTab[(iFilterLen - 1) / 2];
  else
    bTemp = (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2;
  return bTemp;
}
double avergearray(int* arr, int number){
  int i;
  int max,min;
  double avg;
  long amount=0;
  if(number<=0){
    Serial.println("Error number for the array to avraging!/n");
    return 0;
  }
  if(number<5){   //less than 5, calculated directly statistics
    for(i=0;i<number;i++){
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  }else{
    if(arr[0]<arr[1]){
      min = arr[0];max=arr[1];
    }
    else{
      min=arr[1];max=arr[0];
    }
    for(i=2;i<number;i++){
      if(arr[i]<min){
        amount+=min;        //arr<min
        min=arr[i];
      }else {
        if(arr[i]>max){
          amount+=max;    //arr>max
          max=arr[i];
        }else{
          amount+=arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount/(number-2);
  }//if
  return avg;
}

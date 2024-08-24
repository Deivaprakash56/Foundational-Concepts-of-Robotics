# Complementary filter

* A Complementary Filter is a simple and effective technique used to fuse data from different sensors to provide a more accurate and stable output. 

* It combines multiple sensors that **Complement each other's weaknesses with their strengths**.

## Principal working of Complementary filter

* The principle behind a Complementary Filter is to blend the complementary characteristics of the sensors using a 
    * High Pass Filter on one sensor's output
    * Low Pass Filter on another sensor's output.

> So before getting into the concept of complementary filter one should know about the basics of High pass and Low pass filter.

### High Pass Filter
- Allows or lets pass through only the high-frequency signals (quick changes).

- Attenuates or reduces the amplitude of the low-frequency signals (drifts).

### Low Pass Filter
- Allows or lets pass through only the low-frequency signals (stable readings).

- Attenuates or reduces the amplitude of the high-frequency signals.

## Our case of Applying Complementary is on IMU data .

### **IMU (Inertial Measurement Unit)**

  * 6 DOF (Degress of freedom) IMU - Consists of Accelerometer and Gyroscope only.
  * 9 DOF (Degress of freedom) IMU - Consists of Accelerometer , Gyroscope , Magnectometer

![image](https://github.com/user-attachments/assets/fc594ac8-18b4-464c-bdd2-96373ee5c5be)

### Sensor Fusion :

* Sensor fusion is the process of combining data from multiple sensors to get a more accurate and reliable measurement 

* By blending the strengths of each sensor, sensor fusion helps improve the overall than what would be possible using just one sensorunderstanding of the environment or system being measured.

![image](https://github.com/user-attachments/assets/9abd80c4-73bd-486a-9fa3-0f17c94b64e2)

### Implementation of Complementary :

> Now Lets get into the actual topic of Complementary filter 

* As we have discussed in the Principal working of Complementary filter , Now we know that we need to apply high pass filter to one sensor and low pass filter to another sensor for fusion of both the sensor
---

> In our case lets take a 6DOF IMU for sensor fusion and we are going to perform fusion of accelerometer and gyroscope senosors.

* Now at first we need to decide we need to apply the high pass filter and to which do we need to add the low pass filter.

For deciding that  we need to know the nature of data of both the sensors, 

* **Accelerometer** - Fast and noiseless reading.
* **Gyroscope** - Reliable and noisy reading.

By fusing these two sensors we get ,

* **Fused data** - Filtered, reliable, noiseless readings.

![image](https://github.com/user-attachments/assets/784729ed-f790-4b2d-b8fc-76d4a3c6eff1)


### Applying High Pass Filter
* For gyroscope data, this helps in removing the slow drift and focusing on the rapid changes.

* The high-pass filter is typically applied by integrating the **gyroscope rate of change over time** and **combining it with the previous filtered angle**.

        GYRO: {previous_filtered_angle + gyro_rate * Δt}


### Applying Low pass Filter 
* For accelerometer data, this helps in smoothing out the noisy data and focusing on the stable, long-term orientation.

* The low-pass filter is applied by using the accelerometer data to directly calculate the angle.

        ACCEL: {accelerometer_angle}


## Mathematical Formulation of Complementary filter:

![image](https://github.com/user-attachments/assets/d7221152-81c6-4f38-9b1a-5c563272d948)


    Complementary filter = {Low_pass(Accele)} + {High_pass(Gyro)}

      α × [(Gyro)]  + (1−α) × [(Accele)]  

     Filtered_angle = { α × (previous_filtered_angle + gyro_rate × Δt) } + {(1−α)× accel_angle}

* α is the filter coefficient (0 < 𝛼 < 1), typically close to 1.
*  (1−α) is complement of  α

## Conclusion

The Complementary Filter is a powerful yet simple method for sensor fusion, particularly when dealing with IMU data.
 - By effectively combining the strengths of both accelerometers and gyroscopes, the filter provides accurate and stable estimates of orientation.


## Applications of Complementary Filter

1. **Drones and UAVs (Unmanned Aerial Vehicles):**
   - Complementary filters are widely used in drones to maintain stable flight by accurately estimating the orientation (pitch, roll, and yaw) of the aircraft.
   
2. **Robotics:**
   - In mobile robots, complementary filters help in maintaining balance and orientation by fusing data from accelerometers and gyroscopes, especially in bipedal and wheeled robots.

3. **Smartphones and Wearables:**
   - Complementary filters are used in smartphones and wearable devices to track orientation and movement for features like screen rotation, fitness tracking, and gesture recognition.

4. **Virtual Reality (VR) and Augmented Reality (AR):**
   - These filters are essential in VR and AR systems to provide smooth and responsive head-tracking by combining gyroscope and accelerometer data for accurate orientation sensing.

5. **Automotive Industry:**
   - In advanced driver-assistance systems (ADAS) and autonomous vehicles, complementary filters help in stabilizing the sensor data used for navigation and control.

By applying a complementary filter in these areas, the reliability and accuracy of sensor data interpretation are significantly improved, leading to better performance and user experience.




















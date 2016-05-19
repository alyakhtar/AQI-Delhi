# Predict Air Quality Index for Delhi

### Parameters Used - 

* Temperature

* Wind speed

* Relative Humidity

* Traffic index

* Air quality of previous day

* Industrial parameters such as power plant emissions


### Algorithm Used - 

* Support Vector Machine (SVM)
* Naive Bayes
* Other NN algo's


### Variation of PM 2.5 values over the last 3 years (Jan 2013 - Dec 2015)

![ScreenShot](/graphs/PM2.5for4Years.png)


### Data Sources

* [Data for PM 2.5 provided by US Embassy in Delhi](http://newdelhi.usembassy.gov/airqualitydataemb.html)
* [Meteorologiacal Data](http://en.tutiempo.net/climate/01-2015/ws-421820.html)
* Traffic Data provided by CRRI
* [PM 2.5 Ratings](https://en.wikipedia.org/wiki/Air_quality_index#India)


 <table style="width:100%">
   <tr>
    <td><span style="font-weight:bold">PM 2.5</span></td>
    <td><span style="font-weight:bold">Condition</span></td>
    <td><span style="font-weight:bold">Rating</span></td>
  </tr>
  <tr>
    <td>0-30</td>
    <td>Good</td>
    <td>1</td>
  </tr>
  <tr>
    <td>31-60</td>
    <td>Satisfactory</td>
    <td>2</td>
  </tr>
  <tr>
    <td>61-90</td>
    <td>Moderately Polluted</td>
    <td>3</td>
  </tr>
  <tr>
    <td>91-120</td>
    <td>Poor</td>
    <td>4</td>
  </tr>
  <tr>
    <td>121-250</td>
    <td>Very Poor</td>
    <td>5</td>
  </tr>
  <tr>
    <td>250+</td>
    <td>Severe</td>
    <td>6</td>
  </tr>
</table>
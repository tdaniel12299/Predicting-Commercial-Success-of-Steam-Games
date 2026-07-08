<a id="readme-top"></a>

<br />
<div align="center">  

  <h1 align="center">Predicting Commercial Success of Steam Games</h1>

  <p align="center">
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Project Overview</a>
      <ul>
        <li><a href="#built-with">Technologies Used</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Data Cleaning</a></li>
    <li><a href="#usage">EDA</a></li>
    <li><a href="#roadmap">Model Building</a></li>
    <li><a href="#contributing">Model Performance</a></li>
    <li><a href="#license">Insights</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->

## Project Overview


This project explores what features are most closely associated with commerical success across multiple game titles. The ultimate goal is to highlight aspects within the gaming industry that can lead to future successful gaming titles.

Objectives:
* Analyze and define what a "successful" game is using feature engineering
* Opitmize Logistical and Random Forest Regressors to determine best model for predicting
* Identify relationships between games' user-based performance and indiviual tags, genres, and categories


The dataset contains information from 80,000+ game titles across the Steam platform.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Technology Used

Programming & Analysis
* Python
* Pandas
* NumPy
* SciPy
* SciKit-Learn
Data Visualization
* Spyder

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Data Cleaning -->
## Data Cleaning

Cleaning the dataset included:

* Renaming the columns in order to index correctly without unidentited variables
* Splitting the tags, genres, and categories into list in order to parse the information
* Changing the datatypes to the appropriate type per column
* Creating 'Release year' column from the 'Release date' column for linear EDA
* Creating 'Log price' column from the 'Price' column for normalization of data
* Creating 'Game age' column
* Creating 'Total supported languages' column



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## EDA

Below are a few highlights from the dataset after cleaning: 

* After applying a logarithmic transformation, the distribution of game prices remained positively skewed. The median price was approximately $20.67, with 50% of games priced between roughly $10 and $40
* The transformation reduced the influence of extreme values but several high-priced outliers remained, indicating that a subset of games were substantially more expensive than the majority of titles in the dataset. This subset is believed to be games produced by triple A developers (big name companies)
<img width="534" height="413" alt="logPriceGraph" src="https://github.com/user-attachments/assets/ecf68bda-7420-4ff1-af25-8cd351b1c0bc" />




* The line graph indicates slow increase in annual game releases from 1997-2013 and rapid expansion from 2014 to 2019. Peak volumes of released games sits at 22,000 for the year of 2025 which is consist with the develpment of entertainment technology
* Sudden drop of titles suggests incomplete data for the year of 2026
<img width="569" height="432" alt="gameReleasesInYears" src="https://github.com/user-attachments/assets/91960687-8388-428d-a819-ddb1bf1b1d3b" />



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Model Building

**After transforming the categorical variables into MultiLabelBinarizer bins, I split the data into train and test sets with a test size of 20% **
- [x] Logistical Regression - ideal for baseline classicfication of categorical values, in this cause "Successful/Unsuccessful" games
- [x] Random Forest Regressor - focuses on finding feature importance 

  


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MODEL PERFORMANCE -->
## Model Performance

The Random Forest Model slightly outperformed the other approach on the test and validation sets.
* Random Forest: Precision = 72%, F1 = 50%
* Logistical Regression: Precision = 68%, F1 = 43%


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSIGHTS -->
## Insights

* Localization reach appears strongly associated with game success, suggesting that broader language support may increase market accessibility
* Games offering additional Steam features were more likely to be classified as successful
* While LogPrice is heavily utilized within the model, it only suggests that it has an association with game success

 **Overall, specific genre and category of game matter less for future success compared to localization, price point, and built in accessiablity features** 
  
  <img width="1015" height="536" alt="top15PredictorsOfSuccess" src="https://github.com/user-attachments/assets/cbda23cb-4ea3-4307-b795-9bbec6eef200" />



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Tyler Daniel - [@Tyler.Daniel](www.linkedin.com/in/tyler-daniel-1503841ba) 

<!--Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Read-Me Template]([https://choosealicense.com](https://github.com/othneildrew/Best-README-Template/blob/main/README.md))
* [Pandas Cheat Sheet]([https://www.webpagefx.com/tools/emoji-cheat-sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf))
* [NumPy Documentation]([https://flexbox.malven.co/](https://numpy.org/doc/stable/user/absolute_beginners.html))
* [SciPy Documentation]([https://grid.malven.co/](https://docs.scipy.org/doc/scipy/reference/stats.html))


<p align="right">(<a href="#readme-top">back to top</a>)</p>



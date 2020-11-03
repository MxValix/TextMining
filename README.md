# TextMining
Review text and based on it how it impacts the customer decision to recommend the product. <br>
The data set is from Kaggle and contains data about reviews from Women’s Clothing E-Commerce written by customers.

## Introduction

This data set includes 23486 rows and 10 feature variables. Each row corresponds to a customer review. <br>As mentioned in the Overview section on the Kaggle website, the dataset contains the following variables:

<ul>
  <li>Clothing ID</li>
  <li>Age (of the reviewer)</li>
  <li>Title (of review)</li>
  <li>Review</li>
  <li>Rating (out of 5-stars)</li>
  <li>Recommendation index (i.e. whether customer would recommend this product to others: yes= 1/no = 0 )</li>
  <li>Positive Feedback Count (the number of readers who found the review useful)</li>
  <li>Division name (e.g. General Petite, Intimates)</li>
  <li>Department name (e.g. Jackets, Tops, Bottoms)</li>
  <li>Class name (e.g. Blouses, Pants, Skirts, Swim, Knits)</li>
 </ul> 

## Column Details

<ol>
  <li> Clothing ID: Integer Categorical variable that refers to the specific piece being reviewed. </li>
  <li> Age: Positive Integer variable of the reviewers age. </li>
  <li> Title: String variable for the title of the review. </li>
  <li> Review Text: String variable for the review body. </li>
  <li> Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best. </li>
  <li> Recommended IND: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended. </li>
  <li> Positive Feedback Count: Positive Integer documenting the number of other customers who found this review positive. </li>
  <li> Division Name: Categorical name of the product high level division. </li>
  <li> Department Name: Categorical name of the product department name. </li>
  <li> Class Name: Categorical name of the product class name.</li>

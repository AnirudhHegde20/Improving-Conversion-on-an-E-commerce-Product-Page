# Improving-Conversion-on-an-E-commerce-Product-Page

## Introduction

Conversion rate optimization is a critical focus for e-commerce businesses, as even small improvements in conversion rates can result in significant revenue gains. This project uses A/B testing to evaluate the impact of a new product page design (Treatment B) compared to the existing design (Control A). The goal is to determine whether the new design leads to a statistically significant improvement in conversion rates. By leveraging statistical techniques and data-driven insights, this project aids in making informed decisions regarding product page optimization.

## Project Description

This project focuses on analyzing the performance of two different product page designs in terms of conversion rate. Using data collected during the A/B testing process, the project includes exploratory data analysis (EDA), statistical hypothesis testing, and segment analysis to evaluate the effectiveness of the new design. The project employs Python and libraries such as Pandas, Seaborn, Matplotlib, and Scipy for data manipulation, visualization, and analysis.

## Objectives
1.	Formulate the Hypothesis: Clearly define the null and alternative hypotheses for the A/B test.
2.	Analyze Conversion Rates: Compare conversion rates between the two groups to assess Treatment B’s effectiveness.
3.	Statistical Testing: Perform Chi-Square and Fisher’s Exact Tests to determine statistical significance.
4.	Segment Analysis: Explore segment-level performance based on region and device type.
5.	Provide Recommendations: Deliver actionable insights to guide business decisions.

## Data Source

The dataset used in this project is synthetic, simulating real-world e-commerce data. It includes 2,000 observations, split into two groups:

•	Group A (Control): Current product page design.
 
•	Group B (Treatment): New product page design.

Each record contains the following attributes:

	
•	user_id: Unique identifier for each user.
 
•	experiment_group: Indicates whether the user belongs to Group A or B.

•	region: Geographic region of the user.

•	device_type: Device used to access the page (Mobile, Desktop, Tablet).

•	time_spent_seconds: Time spent on the page.

•	added_to_cart: Whether the user added items to the cart.

•	purchase: Whether the user completed a purchase.

## Methodology

### Data Sourcing and Cleaning
•	Loaded the synthetic dataset and checked for missing or duplicate values.

•	Ensured balanced group assignment and no significant biases in attributes such as region or device_type.

### Exploratory Data Analysis (EDA)
•	Visualized conversion rates for both groups.

•	Checked for balanced randomization in demographic attributes (e.g., region, device type).

### Statistical Testing
•	Chi-Square Test: Evaluated overall differences in conversion rates between A and B.

•	Fisher’s Exact Test: Conducted segment-level significance testing for region + device_type.

•	Confidence Intervals: Calculated 95% CIs for conversion rates in both groups.

### Segment Analysis
•	Explored conversion rates across combinations of region and device_type to identify any hidden patterns.

## Key Findings

### Overall Results
•	Group A (Control): Conversion Rate = 7.5%.

•	Group B (Treatment): Conversion Rate = 8.8%.

•	Chi-Square p-value: 0.3316 (not statistically significant).

### Segment Analysis
•	Most sub-segments showed no statistically significant difference between A and B.

•	Notable exception: Europe + Tablet, where B underperformed significantly:

•	CR_A = 18.4%, CR_B = 0.0%, p-value = 0.0151.

### Conclusions
•	No Broad Evidence for Improvement: Overall, the new design (Treatment B) does not show statistically significant improvement over the current design (Control A).

•	Localized Issues: Treatment B performed poorly for the Europe + Tablet segment, suggesting specific usability issues in that context.

•	Targeted Rollout: Consider partial adoption of Treatment B for sub-segments where performance is neutral or slightly better than A, while retaining A for Europe + Tablet users.

## Business Recommendations
1.	Investigate Poor Performance in Europe + Tablet:
•	Analyze page design, load times, or other factors that may contribute to B’s underperformance.
2.	Phased Rollout:
•	Roll out B in segments where performance is comparable or better than A (e.g., North America + Desktop).
3.	Continued Testing:
•	Extend the A/B test with more data to confirm trends and improve confidence levels.
4.	Monitor Key Metrics:
•	Use dashboards to track real-time performance of A and B across user segments.

## Future Scope
1.	Larger Sample Sizes: Increase test duration to gather more data and strengthen the statistical power of the analysis.
2.	Personalization: Use machine learning models to identify user segments most likely to benefit from specific designs.
3.	Multi-Armed Bandit Testing: Explore adaptive testing methods to dynamically allocate traffic to better-performing designs.
4.	New Test Variants: Design and test further iterations (Treatment C, D, etc.) to address the identified weaknesses in B.

## Conclusion

This A/B testing project demonstrates a structured approach to analyzing product page performance using data-driven methods. By combining statistical tests, segment analysis, and actionable business recommendations, this project provides valuable insights into the effectiveness of design changes. The findings emphasize the importance of segment-specific analysis and careful interpretation of test results before implementing global changes. This methodology can serve as a foundation for ongoing optimization efforts in conversion rate improvement.

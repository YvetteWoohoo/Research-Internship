# Research-Internship
This code repository accompanies the paper "Reputation, Collaboration, and Success in the Film Industry: Exploring the Feedback Loop of
Past Performance and Future Opportunities"

film.py
* Fetches movie credit data (cast and crew) from The Movie Database (TMDb) API.
* Reads movie IDs from id_df.csv.
* Saves extracted cast data to cast_data.csv.
* Saves extracted crew data to crew_data.csv.

separate columns.py
* Loads production companies.csv.
* Splits the 'production_companies' column into multiple new columns.

Data cleaning.qmd
* Initial Data Integration: Loads and merges film datasets from TMDB and IMDb.
* Data Cleaning and Filtering: Performs initial cleaning by selecting relevant columns, handling missing values, and removing duplicates.
* Feature Engineering: Creates new variables including categorized genres, runtime, title word count, Oscar nomination dummy, number of production companies, and origin country (US dummy).
* Holiday Dummies: Generates dummy variables for various US holidays based on movie release dates.
* Gender Imputation & Ratios: Processes cast and crew data, imputes missing gender information, and calculates gender ratios (female acting, female crew, total female ratio).
* Financial Imputation: Imputes missing budget and revenue values using various statistical methods (e.g., PMM, CART) and calculates profit-related variables.
* Final Dataset Preparation: Prepares the final cleaned dataset (film_final.csv) for subsequent analysis.

Descriptive Analysis.qmd
* Data Preparation: Recodes key categorical variables (e.g., box, artistic, adult) into more descriptive labels for clarity in analysis.
* Box Office Performance Analysis: Generates descriptive statistics and balance tables to compare film characteristics based on "Box office success" versus "Box office failure".
* Artistic Performance Analysis: Provides descriptive statistics and balance tables to compare film attributes based on "Artistic success" versus "Artistic failure".
* Overall Performance Analysis: Compares film characteristics across "Overall success", "Overall failure", and the full dataset to understand general trends related to combined box office and artistic outcomes.

Network.qmd
* Network Construction: Identifies key actors, directors, and producers; builds various collaboration networks (e.g., actor-actor, director-actor, producer-director) using igraph.
* Network-Level Metrics: Calculates and summarizes global network properties such as node and edge counts, density, average degree, path length, and community structure (e.g., modularity).
* Individual-Level Features: Derives career-related metrics for each professional, including cumulative past profits, career lengths, and historical success/failure rates in different roles.
* Collaboration-Level Features: Computes collaboration-specific variables, such as the number of past collaborations between pairs of individuals and their historical success/failure rates.

Regression.qmd
* Data Preparation: Loads the final merged film dataset and performs necessary transformations (e.g., log transformations, factor conversions) on relevant variables.
* Logistic Regression for Box Office Success: Develops and evaluates a series of logistic regression models to predict box office success, incrementally incorporating film characteristics, individual career histories, and collaboration patterns.
* Logistic Regression for Artistic Success: Develops and evaluates a series of logistic regression models to predict artistic success, similarly building upon film characteristics, individual career histories, and collaboration patterns.
* Linear Regression for Log Revenue: Develops and evaluates a series of linear regression models to predict logarithmic film revenue, also incrementally adding film characteristics, individual career histories, and collaboration patterns as predictors.


<h1>CloudSortInterview</h1>

# markdown ref https://en.wikipedia.org/wiki/Markdown

Exploring different options to visualize PLD data for network optimization 

Code for Collin Wischmeyer's Code Interview 

<h2>Contents:</h2>
- Files
  1. **pld_data_import_munge.py:** File to read in pld data, enrich data and add in requested average per day column

- Directory
  1. **FauxProdCode:** contains the pseudo code to demonstrate how a resuable network optiization app might look like 

<h3>Approach</h3>
- Enrich Zip code information with prebuilt library (https://uszipcode.readthedocs.io/uszipcode/search.html#uszipcode.search.SearchEngine.by_population_density)
     - Obtain state and city information for readability and sementation 

- Build network model with networkx (or similar tool if large data set) 
    - Utilize to find most connected nodes
    - Use connected nodes to generate region subgraphs 
        - Can be repeated to generate regional and subregional hubs 
    - Utilize differing edge weights to analyze system for various optimizations
        -   Pure volume - number of orders 
        -   Delivery time - google api for drive time
        -   Value - Drive time/number of orders 
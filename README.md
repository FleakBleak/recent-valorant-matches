# Valorant Match Results Scraper

This script extracts and displays the results of recent Valorant matches from the esports website vlr.gg. It uses the BeautifulSoup library to scrape and parse the HTML content, providing an easy-to-read format for recent match results.

## How It Works
The script sends an HTTP GET request to the vlr.gg "recent matches" page, then uses BeautifulSoup to parse the HTML content and find the relevant data. It extracts team names and scores from the page and displays them in a simple format: `<team1> <score1> VS <score2> <team2>`. The script handles cleaning the extracted data to ensure it is displayed correctly.

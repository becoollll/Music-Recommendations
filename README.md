# Music Recommendations

This is a Flask web application that provides music recommendations based on user preferences and displays popular music charts. The project leverages Flask for the back-end, along with front-end technologies like HTML, CSS, and JavaScript to create a user-friendly interface.

🔗 Here is the link for this project: [Music Recommendations](https://musicrecommendations.onrender.com/)

## Project Overview

The goal of this project is to build a web application where users can receive music recommendations, view trending music charts, and explore new music genres. Users can select their favorite artists, genres, or songs to get personalized recommendations.

## Features

- **Music Recommendations**: Get personalized music recommendations based on user preferences.
- **Popular Charts**: View the latest music charts from various genres and regions.
- **Genre Exploration**: Discover new genres and explore recommended artists.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or above
- Flask 2.0 or above
- (Other dependencies such as `requests`, `pandas`, etc.)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/becoollll/Music-Recommendations.git
   
2. **Navigate to the project directory:**
   ```bash
   cd Music-Recommendations
   
3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   
4. **Activate the virtual environment:**
    **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ``` 
    **On Windows:**
    ```bash
    venv\Scripts\activate

5. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

### Running the Application

1. **Set the Flask environment variables:**
    **On macOS/Linux:**
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ``` 
    **On Windows:**
    ```bash
    set FLASK_APP=app.py
    set FLASK_ENV=development
2. **Run the application:**
   ```bash
   flask run
   
3. **Open your browser and navigate to:**
   ```bash
   http://127.0.0.1:5000/

### Project Directory Structure
```bash
Music-Recommendations/
│
├── app.py                        # Main application file
├── data_by_genres.csv            # Features dataset
├── getByGenres_all.py            # Recommendations analyze
├── getByGenres_sep.py            # Recommendations analyze
├── getGenres.py                  # Spotipy API connection
├── get_charts.py                 # Spotipy API connection
├── knn_genre.py                  # Spotipy API connection
├── requirements.txt              # Python dependencies
├── Procfile                      # Render deploy file
├── static/                       # Static files (CSS, JavaScript, images)
│   └── style.css                 # Stylesheet for the project
├── templates/                    # HTML templates
│   ├── charts.html               # Chart template
│   └── index.html                # Homepage template
├── music/                        # ipynb files
│   ├── Crawl_TopSongs.ipynb      # Crawl top songs on spotify chart
│   └── KNN_modelTraining.ipynb   # KNN training test
└── README.md                     # Project documentation (this file)
```

### Technologies Used
- **Flask:** Web framework for back-end
- **HTML/CSS:** Front-end structure and styling
- **Music Recommendations:** Get personalized music suggestions.
- **Music Charts:** View popular music charts.






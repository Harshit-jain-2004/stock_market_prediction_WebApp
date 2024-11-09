from setuptools import setup 

setup( 
	name='Stock-Prediction-Web-App', 
	version='0.1', 
	description='Stockprediction web app', 
	author='Harshit Jain', 
	author_email='harshitjain20apr@gmail.com', 
	packages=['Stock-Prediction-Web-App'], 
	install_requires=[ 
		'numpy', 
		'pandas', 
        'matplotlib',
        'streamlit',
        'yfinance',
	], 
) 

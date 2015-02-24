from fresh_tomatoes import open_movies_page
from movie_class import Movie 



'''Use Class Movie which import from fresh_tomatoes_class, 
store movies data as below example:'''

mission = Movie(
	title="The Mission", 
	photo_link="http://upload.wikimedia.org/wikipedia/zh/f/f1/The_Mission_1999.jpg",
	youtube_link="http://youtu.be/u3dePG1ikv8",
	director="Johnnie To",
	)

election = Movie(
	title="Election", 
	photo_link="https://upload.wikimedia.org/wikipedia/en/a/af/Election_2005_Film.JPG",
	youtube_link="http://youtu.be/YY8MbwAK_rE",
	director="Johnnie To",
	)

election2 = Movie(
	title="Election 2", 
	photo_link="https://upload.wikimedia.org/wikipedia/en/6/61/Election2HK.jpg",
	youtube_link="http://youtu.be/uzVp2qyHk4M",
	director="Johnnie To",
	)

# Add new instants to the movies list after create new instants.
movies = [mission, election, election2]


def get_html(movies_list=movies):
	""" 
	get_html() will help you generate a html page.

	parameters:
		movies_list - this is the only param. default value is 'movies'.
		it should be the data list you define.
	"""
	open_movies_page(movies_list)
	# This function is imported from fresh_tomatoes.py. 


if  __name__ == "__main__":
	get_html()


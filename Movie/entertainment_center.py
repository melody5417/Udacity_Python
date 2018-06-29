import media
import fresh_tomatoes

toy_story = media.Movie("Toy story", 
"A story of a boy and his toys", 
"https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=52d1d685908fa0ec7fc7630b1e97594a/d62a6059252dd42a1835151d023b5bb5c9eab843.jpg", 
"https://v.qq.com/x/cover/ncybspecufzln0z.html")

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
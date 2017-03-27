import my_movies
import media

forrest_gump = media.Movie("Forrest Gump", "Forrest Gump is a simple man with a low I.Q. but good intentions. \
	                        He is running through childhood with his best and only friend Jenny. \
	                        His 'mama' teaches him the ways of life and leaves him to choose his destiny.",
	                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
	                        "https://www.youtube.com/watch?v=uPIEn0M8su0")

beautiful_mind = media.Movie("A Beautiful Mind", "A Beautiful Mind is a 2001 American biographical drama film based \
	                          on the life of John Nash, a Nobel Laureate in Economics.",
	                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/A_Beautiful_Mind_Poster.jpg/220px-A_Beautiful_Mind_Poster.jpg",
	                          "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

man_who_knew_infinity = media.Movie("A Man Who Knew Infinity", " A Life of the Genius Ramanujan. \
	                                 In 1913, a twenty-five-year-old Indian clerk with no formal education wrote a letter to G.H. \
	                                 Hardy, then widely acknowledged as the premier English mathematician of his time.",
	                                 "https://upload.wikimedia.org/wikipedia/en/thumb/d/d8/The_Man_Who_Knew_Infinity_%28film%29.jpg/220px-The_Man_Who_Knew_Infinity_%28film%29.jpg",
	                                 "https://www.youtube.com/watch?v=oXGm9Vlfx4w")

shawshank_redemption = media.Movie("Shawshank Redemption", "Bank Merchant Andy Dufresne is convicted of the false murder charges of his wife and her lover, \
	                                and sentenced to life imprisonment at Shawshank prison.",
	                                "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	                                "https://www.youtube.com/watch?v=6hB3S9bIaco")

kung_fu_panda = media.Movie("Kung Fu Panda", "Unexpectedly chosen to fulfill an ancient prophecy, Po's dreams become reality when \
	                         he joins the world of Kung Fu and studies alongside his idols, the legendary Furious Five -- \
	                         Tigress, Crane, Mantis, Viper and Monkey -- under the leadership of their guru, Master Shifu.",
	                         "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg",
	                         "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

ghost_busters = media.Movie("Ghostbusters", "Paranormal researcher Abby Yates (Melissa McCarthy) and physicist Erin Gilbert are trying to prove that ghosts \
							 exist in modern society. When strange apparitions appear in Manhattan, Gilbert and Yates turn to engineer Jillian Holtzmann for help.",
							 "https://upload.wikimedia.org/wikipedia/en/thumb/3/32/Ghostbusters_2016_film_poster.png/220px-Ghostbusters_2016_film_poster.png",
							 "https://www.youtube.com/watch?v=w3ugHP-yZXw")

death_note = media.Movie("Death Note", "Light Yagami (Tatsuya Fujiwara) is a normal, undistinguished college student -- that is, \
	                      until he discovers an odd notebook lying on the ground.",
	                      "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/SNote.jpg/230px-SNote.jpg",
	                      "https://www.youtube.com/watch?v=ELIKAYTDjNc")

steins_gate = media.Movie("Steins Gate", "A scientist's lover and assistant travels through numerous timelines to find out why \
							he keeps disappearing and how to prevent time from erasing him forever.",
							"https://upload.wikimedia.org/wikipedia/en/b/bb/Steins_gate_xbox360.jpg",
							"https://www.youtube.com/watch?v=W2JflmKHi54")
golden_time = media.Movie("Golden Time", "Banri finds himself completely and utterly lost after the big opening ceremonial event and tries to \
						   find his way to the freshman orientation. Along the way, he runs straight into another lost and confused freshman from \
						   the same school, Mitsuo Yanagisawa, and they immediately hit it off.",
						   "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Golden_Time_Volume_1.jpg/230px-Golden_Time_Volume_1.jpg",
						   "https://www.youtube.com/watch?v=Du_LS9aT3q4")

#beautiful_mind.trailer()
movies = [forrest_gump, beautiful_mind, man_who_knew_infinity, shawshank_redemption, kung_fu_panda, ghost_busters, death_note, steins_gate, golden_time]
my_movies.open_movies_page(movies)
# Movie Multiplex Scheduler

This website was developed as the graded project for the UCS2201 - Fundamentals and Practice of Software Development course.


The timetabling solution is a modular program that is built on Python+Django framework. Python was chosen because of its support for garbage collection, automatic memory management, but most importantly, for the way it handles scripts.

The solution implemented is a computationally intensive bruteforce method. We have built a clean and easy-to-use user interface in the form of a web application, made possible using the Django framework.

This web application was built by [Alamelu Kannan](https://github.com/alameluk17/), [Ananya C.B]() and [Adithya Muthukumar]().

## Input

- Information regarding available screens in the theater

    - This information is collected when a particular theater signs up to use the application. The information is stored for usage in the future. This includes the number of screens available in the theater , the maximum number of screenings allotted to each screen and the facilities available in each of the screens. 


- Information regarding movies to be screened in the theater
    - This information is collected for every movie that the theater owners wish to screen in their theater. It includes the language, the release date, the censor rating  and the required facility. The interest score of the movie is obtained from the internet as real time data using GoogleTrends.


This information is taken from the user with the help of simple HTML forms. 


## Output


Using the data given above , the program returns a timetable that maximizes profit for the theater owners. This is done by satisfying the hard constraints of Feature-mapping and the maximum number of shows allotted for a particular movie, that is calculated by the algorithm. All the other information about the movies are considered soft constraints.


This output timetable is displayed to the user as a HTML table.
